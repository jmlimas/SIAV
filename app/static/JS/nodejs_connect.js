    $(document).ready(function(){

    	var objDiv = document.getElementById("comments");
    	objDiv.scrollTop = objDiv.scrollHeight+10;

    	var socket = io.connect('{{ request.META.HTTP_HOST }}', {port: 4000});
    	
    	socket.on('connect', function(){
    		console.log("connect");
    	});
    	
    	var socket = io.connect();
    	console.log('check 1', socket.socket.connected);
    	socket.on('connect', function() {
    		console.log('check 2', socket.socket.connected);
    	});
    	
    	var entry_el = $('#comment');
    	
    	socket.on('message', function(message) {
    		generate('topRight',message);
        //Escape HTML characters
        var data = message.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
        
        //Append message to the bottom of the list
        $('#comments').append('<li>' + data + '</li>');
        window.scrollBy(0, 10000000000);
        entry_el.focus();

        var objDiv = document.getElementById("comments");
        objDiv.scrollTop = objDiv.scrollHeight+10;
    });
    	
    	entry_el.keypress(function(event){

        //When enter is pressed send input value to node server
        if(event.keyCode != 13) return;
        var msg = entry_el.attr('value');
        if(msg){

        	socket.emit('send_message', msg, function(data){
        		console.log(data);
        	});
        	
        //Clear input value   
        entry_el.attr('value', '');
    }


});


    });

    function generate(layout, message) {
    	var n = noty({
    		text        :  message,
    		type        : 'alert',
    		dismissQueue: true,
    		layout      : 'topRight',
    		theme       : 'defaultTheme',
    		timeout: '9000'
    	});
    	console.log('html: ' + n.options.id);
    }

    function generateAll() {
    	generate('topRight');
    }

    $(document).ready(function () {

    	generateAll();

    });