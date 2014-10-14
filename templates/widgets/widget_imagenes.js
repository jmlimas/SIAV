   <script type="text/javascript" language="javascript" src="{{ STATIC_URL }}JS/flexslider/jquery.flexlider-min.js"></script>
   <script type="text/javascript" language="javascript" src="{{ STATIC_URL }}JS/fileuploader.js"></script>

   <script type="text/javascript">
    // $(function(){
    //   SyntaxHighlighter.all();
    // });
    $(window).load(function(){
      $('#carousel').flexslider({
        animation: "slide",
        controlNav: true,
        animationLoop: false,
        slideshow: false,
        itemWidth: 110,
        itemMargin: 1,
        asNavFor: '#slider'
      });

      $('#slider').flexslider({
        animation: "slide",
        controlNav: false,
        animationLoop: false,
        slideshow: false,
        sync: "#carousel",
        start: function(slider){
          $('body').removeClass('loading');
        }
      });
    });
  </script>

   <script>        
function createUploader(){            
  var uploader = new qq.FileUploader( {
    action: "{% url "app.uploads.ajax_upload" avaluo.avaluo_id avaluo.FolioK %}",
    listElement: $('#image-list'),
    element: $('#file-uploader')[0],
    multiple: true,
    onComplete: function( id, fileName, responseJSON ) {
      if( responseJSON.success )
        alert( "Carga exitosa." ) ;
      else
        alert( "Carga fallida!" ) ;
    },
    onAllComplete: function( uploads ) {
                    // uploads is an array of maps
                    // the maps look like this: { file: FileObject, response: JSONServerResponse }
                    //alert( "All complete!" ) ;
                  },
                  params: {
                    'csrf_token': '{{ csrf_token }}',
                    'csrf_name': 'csrfmiddlewaretoken',
                    'csrf_xname': 'X-CSRFToken',
                  },
                } ) ;
}         


</script>

   <script type="text/javascript"> 
$(function() {

              // in your app create uploader as soon as the DOM is ready
            // don't wait for the window to load  
            window.onload = createUploader; 

          });

</script>