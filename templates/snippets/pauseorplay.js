
$('#masiva_button').tooltipster({
  content: $('<button type="button" id="play_button" class="btn btn-sm btn-success cm_stop_or_play" data-toggle="tooltip" data-placement="bottom" title="Activar" style="margin-right: 10px;"><span class="glyphicon glyphicon-play"></span></button><button id="stop_button" type="button" class="btn btn-sm btn-danger cm_stop_or_play" data-toggle="tooltip" data-placement="bottom" title="Detener"><span class="glyphicon glyphicon-stop"></span></button>'),
  contentAsHTML: true,
  interactive: true,
  position: 'bottom',
});

$('.mass_button').tooltipster('show', function() {
});

$('.mass_button').tooltipster('hide', function() {
});

$( ".cm_stop_or_play" ).click(function() {
  var counter = 0, // counter for checked checkboxes
        i = 0       // loop variable

var str = $( "#masiva_button" ).text().trim();
var param = 2;
if(str == "VISITAR"){
    param = 1;
}else if (str == "CAPTURAR"){
    param = 2;
}else if (str == "SALIDA"){
    param = 3;
}


if(($(this).attr('id')) == 'play_button'){
var url = '//SIAV/cambia_estatus/1/'+param;    // final url string
}else if(($(this).attr('id')) == 'stop_button'){
var url = '//SIAV/cambia_estatus/2/'+param;    // final url string
}
// get a collection of objects with the specified 'input' TAGNAME
input_obj = document.getElementsByClassName('form-checkbox');
// loop through all collected objects
for (i = 0; i
< input_obj.length; i++) {
    // if input object is checkbox and checkbox is checked then ...
    if (input_obj[i].type === 'checkbox' && input_obj[i].checked === true) {
        // ... increase counter and concatenate checkbox value to the url string
        counter++;
        url = url + '/' + input_obj[i].value;
    }
}
// display url string or message if there is no checked checkboxes
if (counter >
    0) {
    // remove first "&" from the generated url string
    url = url.substr(1);
    // display final url string
    location.href = url;
    // or you can send checkbox values
    // window.location.href = 'my_page.php?' + url; 
}
else {
    alert("Selecciona al menos una casilla.");
}
});