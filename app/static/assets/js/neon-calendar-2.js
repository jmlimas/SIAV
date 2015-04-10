
jQuery(document).ready(function($) {

  // quick search regex
  var qsRegex;
  
  // init Isotope
  var $container = jQuery('.isotope').isotope({
    itemSelector: '.draggable',
    layoutMode: 'vertical',
    filter: function() {
      return qsRegex ? jQuery(this).text().match( qsRegex ) : true;
    }
  });

  // use value of search field to filter
  var $quicksearch = jQuery('#quicksearch').keyup( debounce( function() {
    console.log($quicksearch.val());
    qsRegex = new RegExp( $quicksearch.val(), 'gi' );
    $container.isotope();
  }, 200 ) );
  
  $('#eliminarEvento_btn').click(function(){

	var singleValues = jQuery( "#eventId" ).html();
	// alert( singleValues );
	deleteEvent(singleValues);


  })



// debounce so filtering doesn't happen every millisecond
function debounce( fn, threshold ) {
  var timeout;
  return function debounced() {
    if ( timeout ) {
      clearTimeout( timeout );
    }
    function delayed() {
      fn();
      timeout = null;
    }
    timeout = setTimeout( delayed, threshold || 100 );
  }
}

    

        $.getJSON("/api/get_visitadores/", {ajax: 'true' }, function (j) {
            var options = '';
                options += '<option value=""></option>';
            for (var i = 0; i < j.length; i++) {
                options += '<option value="' + j[i].value + '">' + j[i].label + '</option>';
            }
            $("#id_Visitadores").html(options);
        })

$('#id_Visitadores').on('change', function() {
  var eventValues = $( "#eventId" ).html();

  updateEvent(eventValues, this.value);

});








    /* initialize the external events
    -----------------------------------------------------------------*/

    $('.draggable').each(function() {

        // create an Event Object (http://arshaw.com/fullcalendar/docs/event_data/Event_Object/)
        // it doesn't need to have a start or end
        var eventObject = {
            title: $.trim($(this).text()) // use the element's text as the event title
        };

        // store the Event Object in the DOM element so we can get to it later
        $(this).data('eventObject', eventObject);

        // make the event draggable using jQuery UI
        $(this).draggable({
            zIndex: 999,
            revert: true, // will cause the event to go back to its
            revertDuration: 0 //  original position after the drag
        });

    });








    function saveEventUpdate(event) {
        url = '/SIAV/calendario/crea_eventos/';

        // Create a copy of the event object
        //data = $.extend({}, event);
        // Replace string date with timestamp (ms since epoch)
        console.log(event);
        if (event.end == undefined) {
            event.end = ""
        };
        if (event.id == undefined) {
            event.id = ""
        };

        var ret_id = '';

        var jqxhr = $.post(url, {
                id: event.id,
                title: event.title,
                start: event.start.valueOf(),
                avaluo_id: event.avaluo_id,
                allDay: event.allDay,
                end: event.end.valueOf()
            }, function(responseData) {
                // swal("Carga exitosa.","","success");
                // Executed on successful update to backend

                // Newly added event
                if (event.id != undefined) {
                    // Get event ID from insert response
                    obj = jQuery.parseJSON(responseData);
                    ret_id = obj.id;
                    event.id = ret_id;

                    // Render the event on the calendar
                    $('#calendar').fullCalendar('renderEvent', event, true);
                }
            })
            .fail(function() {
                swal("Hubo un error procesando la solicitud, intente de nuevo.", "", "err");
            })

    }


    $('.draggable').draggable({
        revert: false, // immediately snap back to original position
        duration: '00:30',
        revertDuration: 0 //
    });



    function deleteEvent(evento_id) {
        url = '/SIAV/calendario/elimina_eventos/';
 
        // Create a copy of the event object
        //data = $.extend({}, event);
        // Replace string date with timestamp (ms since epoch)

        if (evento_id != undefined) {
            event.id = evento_id
        };

        var ret_id = '';

        var jqxhr = $.post(url, {
                id: event.id,
            }, function(responseData) {
                // swal("Carga exitosa.","","success");
                // Executed on successful update to backend

                // Newly added event
                if (event.id == undefined) {
                    // Get event ID from insert response
                    obj = jQuery.parseJSON(responseData);
                    ret_id = obj.id;
                    event.id = ret_id;

                    // Render the event on the calendar
                    $('#calendar').fullCalendar('removeEvents', evento_id);
                    $('#eventContent').dialog("close");
                }
            })
            .fail(function() {
                swal("Hubo un error procesando la solicitud, intente de nuevo.", "", "err");
            })

    }




    function updateEvent(evento_id,visitador_id) {
        url = '/SIAV/calendario/actualiza_visitador/';
 
        // Create a copy of the event object
        //data = $.extend({}, event);
        // Replace string date with timestamp (ms since epoch)

        if (evento_id != undefined) {
            event.id = evento_id
        };

        var ret_id = '';

        var jqxhr = $.post(url, {
                id: event.id,
                visitador_id: visitador_id,
            }, function(responseData) {
                // swal("Carga exitosa.","","success");
                // Executed on successful update to backend

                // Newly added event
                if (event.id == undefined) {
                    // Get event ID from insert response
                    obj = jQuery.parseJSON(responseData);
                    ret_id = obj.id;
                    event.id = ret_id;

                    // Render the event on the calendar
                    $('#calendar').fullCalendar('removeEvents', evento_id);
                    $('#calendar').fullCalendar( 'refetchEvents' );
                    $('#eventContent').dialog("close");
                }
            })
            .fail(function() {
                swal("Hubo un error procesando la solicitud, intente de nuevo.", "", "err");
            })

    }

    $('#calendar').fullCalendar({
        timezone: 'America/Monterrey',
        lang: 'es',
        minTime: "07:00:00",
        maxTime: "19:00:00",
        defaultTimedEventDuration: '00:30:00',
        forceEventDuration: true,
        allDaySlot: true,
        defaultView: 'agendaWeek',
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        events: {
            url: '/SIAV/calendario/carga_eventos/',
            type: 'POST',
            allDay: false,
            error: function() {
                swal('Hubo un error al cargar los eventos, contacte al administrador.', "", "error");
            }
        },
        googleCalendarApiKey: 'AIzaSyAk5zR9LcqsE5UuW9bTYdyqZGzocW-NhPg',
        aspectRatio: 2,
        /*
        events: {
            googleCalendarId: '8887t7tu2lnp4onj4g1lr74vj4@group.calendar.google.com',
            className: 'gcal-event' // an option!
        },*/
        eventStartEditable: true,
        eventDurationEditable: false,
        droppable: true,

        eventClick: function(calEvent, jsEvent, view) {

           // swal(calEvent.title.replace('-', '\n') + '\n' + calEvent.start.toLocaleString(), "", "");


            // change the border color just for fun
            //$(this).css('border-color', 'red');

        },
        drop: function(date, allDay) { // this function is called when something is dropped

            // retrieve the dropped element's stored Event Object
            var originalEventObject = $(this).data('eventObject');

            // we need to copy it, so that multiple events don't have a reference to the same object
            var copiedEventObject = $.extend({}, originalEventObject);

            // assign it the date that was reported
            var tempDate = new Date(date);
            copiedEventObject.start = date;
            copiedEventObject.end = new Date(tempDate.setMinutes(tempDate.getMinutes() + 30));
            //copiedEventObject.allDay = allDay;
            copiedEventObject.allDay = false; //< -- only change
            // render the event on the calendar
            // the last `true` argument determines if the event "sticks" (http://arshaw.com/fullcalendar/docs/event_rendering/renderEvent/)
            //$('#calendar').fullCalendar('renderEvent', copiedEventObject, true);
            saveEventUpdate(copiedEventObject);
            // is the "remove after drop" checkbox checked?
            // if ($('#drop-remove').is(':checked')) {
            // if so, remove the element from the "Draggable Events" list
            $(this).remove();
            // }

        },
        eventDrop: function(event, dayDelta, minuteDelta, allDay, revertFunc) {
            console.log(event);
            saveEventUpdate(event);
        },
		      eventRender: function (event, element) {
			        element.attr('href', 'javascript:void(0);');
			        element.click(function() {
			            jQuery("#startTime").html(moment(event.start).format('MMM Do h:mm A'));
			            jQuery("#endTime").html(moment(event.end).format('MMM Do h:mm A'));
			            jQuery("#eventInfo").html(event.description);
			            jQuery("#eventTitle").html(event.title);
			            jQuery("#eventId").html(event.id);
			            jQuery("#id_Visitadores").val(event.visitador);
			            jQuery("#eventLink").attr('href', event.url);
			            jQuery('#modal-1').modal('show');

			            // jQuery("#eventContent").dialog({ modal: true, title: event.title, width:450,
			            //      buttons :  { 
			            //          "eventLink" : {
			            //              text: "Eliminar",
			            //              href: event.url,
			            //              id: "eventLink",
			            //              click: function(){

			            //               var singleValues = jQuery( "#eventId" ).html();
			            //               // alert( singleValues );
			            //               deleteEvent(singleValues);

			            //              }   
			            //           }}});

			        });

			    },
    });


});


