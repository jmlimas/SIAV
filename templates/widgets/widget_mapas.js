{% load currency %}

<script type="text/javascript" src="https://maps.google.com/maps/api/js?sensor=true"></script>
<script type="text/javascript" src="{{ STATIC_URL }}JS/infobox/infobox.js"></script>
<link rel="stylesheet" href="{{ STATIC_URL }}CSS/google_maps/infobox.css" type="text/css" media="screen" />

<script type="text/javascript">

{% if avaluo.LatitudG %}

       var latsign = 1;
            if( {{avaluo.LatitudG}} < 0){
                latsign = -1;
            }
            var lonsign = 1;
            if( {{avaluo.LongitudG}} < 0){
                lonsign = -1;
            }
            var declat = Math.round(
                 Math.abs( Math.round({{avaluo.LatitudG}}* 1000000.00)) +
                 (Math.abs(Math.round({{avaluo.LatitudM}}* 1000000.00))/60) +
                 (Math.abs(Math.round({{avaluo.LatitudS}}* 1000000.00))/3600)
            ) * latsign/1000000;

            var declon = Math.round(
                 Math.abs( Math.round(({{avaluo.LongitudG}})* 1000000.00)) +
                 (Math.abs(Math.round(({{avaluo.LongitudM}})* 1000000.00))/60) +
                 (Math.abs(Math.round(({{avaluo.LongitudS}})* 1000000.00))/3600)
            ) * lonsign/1000000;
            {% endif %}

 </script>

// <script type="text/javascript" language="javascript" src="{{ STATIC_URL }}JS/mapas.js"></script>


<script type="text/javascript">


{% if decimal.declon %}
function initialize() {

 var latlng = new google.maps.LatLng({{decimal.declon}},({{decimal.declat}}*-1));
 var myOptions = {
  zoom: 13,
  scrollwheel: false,
  center: latlng,
  mapTypeId: google.maps.MapTypeId.ROADMAP
};
var map = new google.maps.Map(document.getElementById("map_canvas"),
  myOptions);


marker = new google.maps.Marker({
  position: latlng,
  map: map
});

marker.setMap(map);

{% for x in cercanos %}
var latlng = new google.maps.LatLng({{x.2}},({{x.3}}*-1));

marker_{{x.1}} = new google.maps.Marker({
  position: latlng,
  map: map,
  icon:'{{ STATIC_URL }}CSS/images/blue-dot.png'
});
marker_{{x.1}}.setMap(map);

var boxText = document.createElement("div");
boxText.setAttribute('id', 'infobox');
boxText.style.cssText = "margin-top: 0px; background: #fff; padding: 5px;font-size:15px;";
boxText.innerHTML ="<img class='image' src='{% if x.6.strip %}/{{x.6}}{% else %}{{ STATIC_URL }}CSS/images/missing-image.png{% endif %}'/><a href='/SIAV/respuesta_consulta_sencilla/{{x.1}}' target='_blank' ><div class='title'>{{x.4}}</div></a><div class='area'><span class='key'>MTerr:  </span><span class='value'>{{x.7|default:"0.0"}}m<sup>2</sup></span></div><div class='area'><span class='key'>MConst: </span><span class='value'>{{x.8|default:"0.0"}}m<sup>2</sup></span></div><div class='price'>{{x.5|currency}}</div>";

var myOptions_{{x.1}} = {
 content: boxText
 ,disableAutoPan: false
 ,maxWidth: 0
 ,pixelOffset: new google.maps.Size(-140, 0)
 ,zIndex: null
 ,boxStyle: { 
  background: "url('{{ STATIC_URL }}CSS/images/tipbox.gif') no-repeat"
  ,opacity: 0.85
  ,width: "280px"
}
// ,closeBoxMargin: "0px 2px 2px 2px"
,closeBoxURL: "{{ STATIC_URL }}CSS/images/close.gif"
,infoBoxClearance: new google.maps.Size(1, 1)
,isHidden: false
,pane: "floatPane"
,enableEventPropagation: false
};


var ib = new InfoBox();

google.maps.event.addListener(marker_{{x.1}}, "click", function (e) {
  ib.close();
  ib.setOptions(myOptions_{{x.1}})
  ib.open(map, this);
});




{% endfor %}
}

initialize();


{% endif %}
</script>

