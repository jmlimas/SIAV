   <script type="text/javascript" language="javascript" src="{{ STATIC_URL }}JS/flexslider/jquery.flexlider-min.js"></script>
   <script type="text/javascript" language="javascript" src="{{ STATIC_URL }}JS/jquery.fine-uploader.js"></script>



   <script type="text/javascript">
    // jQuery(function(){
    //   SyntaxHighlighter.all();
    // });


    jQuery(window).load(function(){
      jQuery('#carousel').flexslider({
        animation: "slide",
        controlNav: true,
        animationLoop: false,
        slideshow: false,
        itemWidth: 110,
        itemMargin: 1,
        asNavFor: '#slider'
      });

      jQuery('#slider').flexslider({
        animation: "slide",
        controlNav: false,
        animationLoop: false,
        slideshow: false,
        sync: "#carousel",
        start: function(slider){
          jQuery('body').removeClass('loading');
        }
      });
    });
  </script>


  <script>
    // Wait until the DOM is 'ready'
    jQuery(document).ready(function () {
        jQuery("#fine-uploader").fineUploader({
            debug: true,
            request: {
                endpoint: "{% url "app.uploads.ajax_upload" avaluo.avaluo_id avaluo.Folio %}",
            },
            retry: {
               enableAuto: false
            }
        }).on('complete', function (event, fileId, fileName, responseJSON, xhr) {
        if (responseJSON.success === true) {
            sweetAlert( "Carga exitosa.",fileName,"success" ) ;
        } else {
            sweetAlert( "Carga fallida!",fileName,"error" ) ;
        }});
      });
    </script>
 <script type="text/template" id="qq-template">
        <div class="qq-uploader-selector qq-uploader">
            <div class="qq-upload-drop-area-selector qq-upload-drop-area" qq-hide-dropzone>
                <span>Arrastra archivos aqui...</span>
            </div>

            <div class="qq-upload-button-selector btn btn-danger" style="width: auto;"><i class="glyphicon glyphicon-upload"></i> Subir Archivo</div>

            <span class="qq-drop-processing-selector qq-drop-processing">
                <span>Procesando archivos...</span>
                <span class="qq-drop-processing-spinner-selector qq-drop-processing-spinner"></span>
            </span>
            <ul class="qq-upload-list-selector qq-upload-list">
                <li>
                    <div class="qq-progress-bar-container-selector progress">
                      <div class="qq-progress-bar-selector bar"></div>
                    </div>
                    <span class="qq-upload-spinner-selector qq-upload-spinner"></span>
                    <span class="qq-edit-filename-icon-selector qq-edit-filename-icon"></span>
                    <span class="qq-upload-file-selector qq-upload-file"></span>
                    <input class="qq-edit-filename-selector qq-edit-filename" tabindex="0" type="text">
                    <span class="qq-upload-size-selector qq-upload-size"></span>
                    <a class="qq-upload-cancel-selector qq-upload-cancel" href="#">Cancelar</a>
                    <a class="qq-upload-retry-selector qq-upload-retry" href="#">Reintentar</a>
                    <a class="qq-upload-delete-selector qq-upload-delete" href="#">Eliminar</a>
                    <span class="qq-upload-status-text-selector qq-upload-status-text"></span>
                </li>
            </ul>
        </div>
    </script>






