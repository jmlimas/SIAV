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


# Create your views here.




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
 
    # save the file
    #success = save_upload( upload, filename, is_raw, folio_k)

    file_contents = SimpleUploadedFile(filename, request.body)

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
    #Crear evento
    #Eventos.objects.create(user=request.user, evento='SUBIR_FOTO',avaluo=a)

    # let Ajax Upload know whether we saved it or not
    import json
    ret_json = { 'success': 'test','ext':ext }
    return HttpResponse( json.dumps( ret_json ) )

