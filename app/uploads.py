from django.middleware.csrf import get_token
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import SimpleUploadedFile
from app.models import *
import os


# Create your views here.
"""
def upload_page( request ):
  ctx = RequestContext( request, {
    'csrf_token': get_token( request ),
  } )
  return render_to_response('home/selecciona_estado.html', ctx )
"""

def save_upload( uploaded, filename, raw_data,  folio_k):
  ''' 
  raw_data: if True, uploaded is an HttpRequest object with the file being
            the raw post data 
            if False, uploaded has been submitted via the basic form
            submission and is a regular Django UploadedFile in request.FILES
  '''
  try:
    from io import FileIO, BufferedWriter
    d = os.path.dirname("media\\"+folio_k+"\\"+filename)
    if not os.path.exists(d):
      os.makedirs(d)
    with BufferedWriter( FileIO( "media\\"+folio_k+"\\"+filename, "wb" ) ) as dest:
      # if the "advanced" upload, read directly from the HTTP request

      # with the Django 1.3 functionality
      if raw_data:
        foo = uploaded.read( 1024 )
        while foo:
          dest.write( foo )
          foo = uploaded.read( 1024 ) 
      # if not raw, it was a form upload so read in the normal Django chunks fashion
      else:
        for c in uploaded.chunks( ):
          dest.write( c )

      # got through saving the upload, report success
      return True
  except IOError:
    # could not open the file most likely
    pass
  return False
 
def ajax_upload( request,avaluo_id,folio_k ):
  if request.method == "POST":    
    if request.is_ajax( ):
      # the file is stored raw in the request
      upload = request
      is_raw = True
      # AJAX Upload will pass the filename in the querystring if it is the "advanced" ajax upload
      try:
        filename = request.GET[ 'qqfile' ]
      except KeyError: 
        return HttpResponseBadRequest( "AJAX request not valid" )
    # not an ajax upload, so it was the "basic" iframe version with submission via form
    else:
      is_raw = False
      if len( request.FILES ) == 1:
        # FILES is a dictionary in Django but Ajax Upload gives the uploaded file an
        # ID based on a random number, so it cannot be guessed here in the code.
        # Rather than editing Ajax Upload to pass the ID in the querystring,
        # observer that each upload is a separate request,
        # so FILES should only have one entry.
        # Thus, we can just grab the first (and only) value in the dict.
        upload = request.FILES.values( )[ 0 ]
      else:
        raise Http404( "Bad Upload" )
    
    filename2 = folio_k + "/" + filename
    # save the file
    success = save_upload( upload, filename, is_raw, folio_k)

    file_contents = SimpleUploadedFile(filename, request.raw_post_data)


    imagen_avaluo = ImagenAvaluo()
    imagen_avaluo.avaluo_id = avaluo_id
    imagen_avaluo.imagen.save(filename2,file_contents, save=True)
 
    # let Ajax Upload know whether we saved it or not
    import json
    ret_json = { 'success': success, }
    return HttpResponse( json.dumps( ret_json ) )
