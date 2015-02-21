from django.middleware.csrf import get_token
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import SimpleUploadedFile
from app.models import *
from io import FileIO, BufferedWriter
from websock.models import Eventos
import imghdr
import os
import os.path
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import render_to_response
import settings
# Create your views here.



@csrf_exempt    

def ajax_upload( request,avaluo_id,folio_k ):
  filename = "Undefined.jpg"
  file_contents = "Undefined.jpg"
  ext = ""
  if request.method == "POST":    
    if request.is_ajax( ):
      # the file is stored raw in the request
      upload = request
      is_raw = True
      # AJAX Upload will pass the filename in the querystring if it is the "advanced" ajax upload
      
      try:
          if 'qqfile' in request.FILES:
            upload = request.FILES.values( )[ 0 ]
            file_contents = SimpleUploadedFile(upload.name, upload.read())
            imagen_avaluo = ImagenAvaluo()
            imagen_avaluo.avaluo_id = avaluo_id
            imagen_avaluo.FolioK = folio_k
            imagen_avaluo.imagen.save(upload.name, file_contents)
            return HttpResponse('Guardado Exitosamente');
          else:
              filename = request.GET['qqfile']
              file_contents = SimpleUploadedFile(filename, request.body)
      except KeyError: 
        return HttpResponse("Ajax request error.");
    # not an ajax upload, so it was the "basic" iframe version with submission via form

      ext = os.path.splitext(filename)[1]

      if (ext == ".png")|(ext == ".jpg")|(ext == ".jpeg")|(ext == ".PNG")|(ext == ".JPG")|(ext == ".JPEG"):
        imagen_avaluo = ImagenAvaluo()
        imagen_avaluo.avaluo_id = avaluo_id
        imagen_avaluo.FolioK = folio_k
        imagen_avaluo.imagen.save(filename.replace(' ','_'), file_contents)
      else:
        archivo_avaluo = ArchivoAvaluo()
        archivo_avaluo.avaluo_id = avaluo_id
        archivo_avaluo.FolioK = folio_k
        archivo_avaluo.file.save(filename.replace(' ','_'), file_contents)
      a = Avaluo.objects.get(FolioK=folio_k)
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
        #file_contents = SimpleUploadedFile(filename, upload.content)
      # save the file
        success = save_upload( upload, filename, is_raw, folio_k)
      else:
        raise Exception('Bad Upload')
     

    #Crear evento
    #Eventos.objects.create(user=request.user, evento='SUBIR_FOTO',avaluo=a)

    # let Ajax Upload know whether we saved it or not
    import json
    ret_json = { 'success': 'test','ext':ext }
    return HttpResponse( json.dumps( ret_json ) )

def save_upload( uploaded, filename, raw_data, folio_k ):
  ''' 
  raw_data: if True, uploaded is an HttpRequest object with the file being
            the raw post data 
            if False, uploaded has been submitted via the basic form
            submission and is a regular Django UploadedFile in request.FILES
  '''
  #filename = settings.MEDIA_ROOT + "/" + filename 
  filename = os.path.join('media/',str(folio_k), filename)
  # print settings.MEDIA_ROOT
  # print settings.UPLOAD_STORAGE_DIR
  # print filename
  try:
    from io import FileIO, BufferedWriter
    with BufferedWriter( FileIO( filename, "wb" ) ) as dest:
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
