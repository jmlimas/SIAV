  
 function initialize() {

   var latlng = new google.maps.LatLng(declon,(declat*-1));
   var myOptions = {
      zoom: 14,
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

	
	
	  
	}
	
	    // Function for adding a marker to the page.