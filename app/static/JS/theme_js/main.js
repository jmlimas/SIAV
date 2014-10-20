jQuery(document).ready(function($) {
   'use strict';	
 
   /* ==============================================
		MODERNIZR
	=============================================== */
	Modernizr.load({
	  	test: Modernizr.input.placeholder,
	  	nope: 'js/placeholder.js',
	  	complete : function () {
			if(!Modernizr.input.placeholder) {
      			$('input, textarea').placeholder();
			}
		}
	});
	
	/* ==============================================
		PULSE FALLBACK
	=============================================== */
	if(!Modernizr.cssanimations) {
		$('.btn').addClass('btn-noanimated');
	}
	
   /* ==============================================
		WAYPOINTS
	=============================================== */	
	
	// Only load parallax when not on mobile devices
	if( !/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
		
		$('.animated').waypoint(function() {
			$(this).each(function(){
				var animation = $(this).attr( "data-animation" );
				$(this).addClass( animation );
				$(this).addClass( 'visible' );
			});
		},
		{
			offset: '70%',
			triggerOnce: true
		});
	
	} else {
		
		$('.animated').addClass( 'visible' );
	
	}
	
	$('#about').waypoint(function() {		
			$('#about .progress-bar').each(function(){
				var percent = $(this).attr( "data-value" ) + '%';
				$(this).css( "width", percent );
			});
		},
		{
			offset: '70%',
			triggerOnce: true
		});
		
	/* ==============================================
		MMENU
	 =============================================== */	
   
	function mmenuw() {
		var wi = $(window).width();
		var nb = $("#mmenu-side-menu").length;
		if(wi < 760) {
			if(nb < 1) {
				$('#side-menu').clone( true ).attr("id", "mmenu-side-menu").appendTo( "body" ).mmenu({
					position: "right",
					zposition:"front",
					moveBackground:false,
					clone:true,
					dragOpen:true,
					});
				$('#mmenu-side-menu ul').removeClass('nav navbar-nav navbar-right');
			}
		}
	}
	
	function mmenuw_class() {
		var wi = $(window).width();
		if(wi < 992) {
			$('#nav .container').addClass('container-fluid');
			$('#nav .container').removeClass('container');
		} else {
			$('#nav .container-fluid').addClass('container');
			$('#nav .container-fluid').removeClass('container-fluid');
		}
	}
		
	mmenuw();
	mmenuw_class();
	$(window).resize(function() { 
		mmenuw();
		mmenuw_class();
	});
   
	/* ==============================================
		Count Factors
	 =============================================== */
	 
	 (function($) {
		$.fn.countTo = function(options) {
			// merge the default plugin settings with the custom options
			options = $.extend({}, $.fn.countTo.defaults, options || {});
	
			// how many times to update the value, and how much to increment the value on each update
			var loops = Math.ceil(options.speed / options.refreshInterval),
				increment = (options.to - options.from) / loops;
	
			return $(this).each(function() {
				var _this = this,
					loopCount = 0,
					value = options.from,
					interval = setInterval(updateTimer, options.refreshInterval);
	
				function updateTimer() {
					value += increment;
					loopCount++;
					$(_this).html(value.toFixed(options.decimals));
	
					if (typeof(options.onUpdate) == 'function') {
						options.onUpdate.call(_this, value);
					}
	
					if (loopCount >= loops) {
						clearInterval(interval);
						value = options.to;
	
						if (typeof(options.onComplete) == 'function') {
							options.onComplete.call(_this, value);
						}
					}
				}
			});
		};
	
		$.fn.countTo.defaults = {
			from: 0,  // the number the element should start at
			to: 100,  // the number the element should end at
			speed: 1000,  // how long it should take to count between the target numbers
			refreshInterval: 100,  // how often the element should be updated
			decimals: 0,  // the number of decimal places to show
			onUpdate: null,  // callback method for every time the element is updated,
			onComplete: null,  // callback method for when the element finishes updating
		};
	})(jQuery);	
	 
	 function countUp() {	
			var dataperc;	
			$('.fact-number').each(function(){
				dataperc = $(this).attr('data-perc'),
				$(this).find('.factor').delay(6000).countTo({
					from: 10,
					to: dataperc,
					speed: 1000,
					refreshInterval: 10,
				});  
			});
		}
		
	$('.fact-number').waypoint(function() {
		countUp();
	},
	{
		offset: '70%',
		triggerOnce: true
	});
	   
   /* ==============================================
		BUTTON TO TOP
	=============================================== */	
	// fade in #back-top
	$(function () {
		// scroll body to 0px on click
		$('#back-top').click(function () {
			$('body,html').animate({
				scrollTop: 0
			}, 3000);
			return false;
		});
	});
	
	/* ==============================================
		OWL CAROUSEL
	=============================================== */
	
	$("#quote-slider").owlCarousel({
	  	singleItem:true,
	  });
	
	$("#clients-slider").owlCarousel({
	   	pagination:false,
	  	itemsCustom: [
                        [0, 2],
                        [450, 3],
                        [600, 4],
                        [700, 4],
                        [1000, 5],
                        [1200, 6],
                        [1400, 7],
                        [1600, 7]
                    ],
	  });
   
 
  $("#blog-slider").owlCarousel({
	  pagination:false,
	  itemsCustom: [
                        [0, 2],
                        [450, 1],
                        [600, 2],
                        [700, 2],
                        [1000, 2],
                        [1200, 3],
                        [1400, 4],
                        [1600, 5]
                    ],
	  });
	
	 /* ==============================================
		TOOLTIP
	=============================================== */
	jQuery('[data-toggle~="tooltip"]').tooltip({
		container: 'body'
	});

   
   /* ==============================================
		MIXITUP PORTFOLIO
	=============================================== */	
	//Mixitup
	$(function(){
    	$('.home-projects').mixItUp();  
	});
	
	/* ==============================================
		PRETTYPHOTO
	=============================================== */	
	//prettyPhoto
	$("a[data-pretty^='prettyPhoto']").prettyPhoto({
		allow_resize: true, /* Resize the photos bigger than viewport. true/false */
		default_width: 1000,
		default_height: 660,
	   	social_tools:false,
		markup: '<div class="pp_pic_holder"> \
						<div class="pp_top"> \
							<div class="pp_left"></div> \
							<div class="pp_middle"></div> \
							<div class="pp_right"></div> \
						</div> \
						<div class="pp_content_container"> \
							<div class="pp_left"> \
							<div class="pp_right"> \
								<div class="pp_content"> \
									<div class="pp_loaderIcon"></div> \
									<div class="pp_fade"> \
										<a href="#" class="pp_expand" title="Expand the image">Expand</a> \
										<div class="pp_hoverContainer"> \
											<a class="pp_next" href="#">next</a> \
											<a class="pp_previous" href="#">previous</a> \
										</div> \
										<div id="pp_full_res"></div> \
										<div class="pp_details"> \
											<div class="pp_nav"> \
												<a href="#" class="pp_arrow_previous">Previous</a> \
												<p class="currentTextHolder">0/0</p> \
												<a href="#" class="pp_arrow_next">Next</a> \
											</div> \
											<p class="pp_description"> \
											<div class="ppt">&nbsp;</div> \
											</p> \
											{pp_social} \
											<a class="pp_close" href="#">Close</a> \
										</div> \
									</div> \
								</div> \
							</div> \
							</div> \
						</div> \
						<div class="pp_bottom"> \
							<div class="pp_left"></div> \
							<div class="pp_middle"></div> \
							<div class="pp_right"></div> \
						</div> \
					</div> \
					<div class="pp_overlay"></div>',
	});   
 
 	/* ==============================================
		PARALLAX
	=============================================== */	
	
	// Only load parallax when not on mobile devices
	if( !/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
		$('.image1').parallax("0%", -0.3);
		$('.image2').parallax("0%", -0.3);
		$('.image3').parallax("0%", -0.3); 
	}
	   
   /* ==============================================
		SUPERSLIDER + HAMMER
	=============================================== */	

	$('#slides').superslides({
		animation: "fade",
		slide_speed: 100,
		pagination: false,
		scrollable: true,
		play: 9000,
	});
	
	$('#slides').ontouchmove = function(e) {
		e.preventDefault();
	 };
	 $('#slides').hammer().on('dragleft', function(e) {
		 e.gesture.preventDefault();
		$(this).superslides('animate', 'next');
	});
	
	$('#slides').hammer().on('dragright', function(e) {
		e.gesture.preventDefault();
		$(this).superslides('animate', 'prev');
	});

	
	/* ==============================================
		NAV
	=============================================== */	
	$("#nav").sticky({
		topSpacing: 0
	});
	
	$('.home-nav').onePageNav({
		scrollSpeed: 1200,
		currentClass: 'active',
		changeHash: true,
		filter: ':not(.external)'
	});
	
	
	/* ==============================================
		AJAX CONTACT FORM
	=============================================== */	
	$('#contactform').submit(function(){

		var action = $(this).attr('action');

		$("#message").slideUp(750,function() {
		$('#message').hide();

 		$('#submit')
			.after('<img src="/static/CSS/loading.gif" class="loader" />')
			.attr('disabled','disabled');

		$.post(action, {
			Nombre: $('#id_Nombre').val(),
			Correo: $('#id_Correo').val(),
			Telefono: $('#id_Telefono').val(),
			Mensaje: $('#id_Mensaje').val(),
		},
			function(data){
				document.getElementById('message').innerHTML = data;
				$('#message').slideDown('slow');
				$('#contactform img.loader').fadeOut('slow',function(){$(this).remove()});
				$('#submit').removeAttr('disabled');
				if(data.match('success') != null) $('#contactform').slideUp('slow');

			}
		);

		});

		return false;

	});

	
});
//End Document.ready

	
$(window).load(function() {
	'use strict';
	
	/* ==============================================
		PAGE LOADER
	=============================================== */
	
	$(".loader-item").delay(7000).fadeOut();
	$("#pageloader").delay(12000).fadeOut("slow");
	
});
//End window.load