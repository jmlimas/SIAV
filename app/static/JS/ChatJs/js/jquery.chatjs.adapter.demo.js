
/// <reference path="jquery.chatjs.adapter.ts" />
var DemoAdapterConstants = (function () {




    function DemoAdapterConstants() {
    }
    DemoAdapterConstants.CURRENT_USER_ID = 1;

    DemoAdapterConstants.ECHOBOT_USER_ID = 2;

    DemoAdapterConstants.ECHOBOT_USER3_ID = 3;

    DemoAdapterConstants.DEFAULT_ROOM_ID = 1;

    DemoAdapterConstants.ECHOBOT_TYPING_DELAY = 100;

    DemoAdapterConstants.ECHOBOT_REPLY_DELAY = 500;
    return DemoAdapterConstants;
})();

var DemoClientAdapter = (function () {
    function DemoClientAdapter() {
        this.messagesChangedHandlers = [];
        this.typingSignalReceivedHandlers = [];
        this.userListChangedHandlers = [];
    }
    // adds a handler to the messagesChanged event
    DemoClientAdapter.prototype.onMessagesChanged = function (handler) {
        this.messagesChangedHandlers.push(handler);
    };

    // adds a handler to the typingSignalReceived event
    DemoClientAdapter.prototype.onTypingSignalReceived = function (handler) {
        this.typingSignalReceivedHandlers.push(handler);
    };

    // adds a handler to the userListChanged event
    DemoClientAdapter.prototype.onUserListChanged = function (handler) {
        this.userListChangedHandlers.push(handler);
    };

    DemoClientAdapter.prototype.triggerMessagesChanged = function (message) {
        for (var i = 0; i < this.messagesChangedHandlers.length; i++)
            this.messagesChangedHandlers[i](message);
    };

    DemoClientAdapter.prototype.triggerTypingSignalReceived = function (typingSignal) {
        for (var i = 0; i < this.typingSignalReceivedHandlers.length; i++)
            this.typingSignalReceivedHandlers[i](typingSignal);
    };

    DemoClientAdapter.prototype.triggerUserListChanged = function (userListChangedInfo) {
        for (var i = 0; i < this.userListChangedHandlers.length; i++)
            this.userListChangedHandlers[i](userListChangedInfo);
    };
    return DemoClientAdapter;
})();

var DemoServerAdapter = (function () {
    function DemoServerAdapter(clientAdapter) {
        this.clientAdapter = clientAdapter;


        this.users = new Array();

        // configuring users
        // var myUser = new ChatUserInfo();
        // myUser.Id = DemoAdapterConstants.CURRENT_USER_ID;
        // myUser.RoomId = DemoAdapterConstants.DEFAULT_ROOM_ID;
        // myUser.Name = "André Pena";
        // myUser.Email = "andrerpena@gmail.com";
        // myUser.ProfilePictureUrl = "http://www.gravatar.com/avatar/574700aef74b21d386ba1250b77d20c6.jpg";
        // myUser.Status = 1 /* Online */;

        // Echobot is the guy that will repeat everything you say
        // var echoBotUser = new ChatUserInfo();
        // echoBotUser.Id = DemoAdapterConstants.ECHOBOT_USER_ID;
        // echoBotUser.RoomId = DemoAdapterConstants.DEFAULT_ROOM_ID;
        // echoBotUser.Name = "Echobot Mom";
        // echoBotUser.Email = "echobot1984@gmail.com";
        // echoBotUser.ProfilePictureUrl = "http://www.gravatar.com/avatar/4ec6b20c5fed48b6b01e88161c0a3e20.jpg";
        // echoBotUser.Status = 1 /* Online */;



        var arr= new Array();
        $.each(data, function(i, obj) {
          //use obj.id and obj.name here, for example:
        // Echobot is the guy that will repeat everything you say
        var echoBotUser2 = new ChatUserInfo();
        echoBotUser2.Id = obj[1];   // Id de usuario user.id Django
        echoBotUser2.RoomId = DemoAdapterConstants.DEFAULT_ROOM_ID;
        echoBotUser2.Name = obj[0];
        echoBotUser2.Email = "echobot1954@gmail.com";
        echoBotUser2.ProfilePictureUrl = "http://www.gravatar.com/avatar";
        echoBotUser2.Status = 1 /* Online */;
        arr.push(echoBotUser2);
        // console.log(arr);
          // alert(obj);
        });

        // var echoBotUser2 = new ChatUserInfo();
        // echoBotUser2.Id = DemoAdapterConstants.ECHOBOT_USER3_ID;   // Id de usuario user.id Django
        // echoBotUser2.RoomId = DemoAdapterConstants.DEFAULT_ROOM_ID;
        // echoBotUser2.Name = "{{u.first_name}}";
        // echoBotUser2.Email = "echobot1954@gmail.com";
        // echoBotUser2.ProfilePictureUrl = "http://www.gravatar.com/avatar";
        // echoBotUser2.Status = 1 /* Online */;


        // adds the users in the global user list
        
        this.users = arr;

        // this.users.push(myUser);
        // this.users.push(echoBotUser);
        // this.users.push(echoBotUser2);

        // configuring rooms
        var defaultRoom = new ChatRoomInfo();
        defaultRoom.Id = 1;
        defaultRoom.Name = "Default Room";
        defaultRoom.UsersOnline = this.users.length;

        this.rooms = new Array();
        this.rooms.push(defaultRoom);

        // configuring client to return every event to me
        this.clientAdapter.onMessagesChanged(function (message) {
            return function () {
            };
        });
    }


        // socket.on('chat_receive', function(message) {
        // });

    DemoServerAdapter.prototype.sendMessage = function (roomId, conversationId, otherUserId, messageText, clientGuid, done) {
        var _this = this;
        console.log("DemoServerAdapter: sendMessage");
        // we have to send the current message to the current user first
        // in chatjs, when you send a message to someone, the same message bounces back to the user
        // just so that all browser windows are synchronized
        var bounceMessage = new ChatMessageInfo();
        bounceMessage.UserFromId = current_user_id; // It will from our user  ( Se define con el id de usuario actual)
        bounceMessage.UserToId = otherUserId; // ... to the Echobot   ( Se define con el id del usuario al que se le enviará el mensaje)
        bounceMessage.RoomId = roomId;
        bounceMessage.ConversationId = conversationId;
        bounceMessage.Message = messageText;
        bounceMessage.ClientGuid = clientGuid;

        socket.emit('send_message', bounceMessage, function(data) {
            console.log(bounceMessage.Message);
        });
        console.log(bounceMessage.Message);

        // setTimeout(function () {
            _this.clientAdapter.triggerMessagesChanged(bounceMessage);
        // }, 300);

        // now let's send a message as if it was from the Echobot
        // setTimeout(function () {
            _this.getUserInfo(otherUserId, function (echobotUserInfo) {
                var typingSignal = new ChatTypingSignalInfo();
                typingSignal.ConversationId = conversationId;
                typingSignal.RoomId = roomId;
                typingSignal.UserFrom = echobotUserInfo;

                // if it's not a private message, the echo message will be to the current user
                if (!roomId && !conversationId)
                    typingSignal.UserToId = current_user_id;


                // _this.clientAdapter.triggerTypingSignalReceived(typingSignal);

                // setTimeout(function () {
                    // if otherUserId is not null, this is a private message
                    // if roomId is not null, this is a message to a room
                    // if conversationId is not null, this is a message to a conversation (group of people talking as if it was a room)
                    socket.on('chat_receive', function(message) {
                    console.log(message);
                    var echoMessage = new ChatMessageInfo();
                    echoMessage.UserFromId = message.send_user_id; // It will be from Echobot
                    // echoMessage.UserFromId = 4;
                    echoMessage.RoomId = roomId;
                    echoMessage.ConversationId = conversationId;
                    echoMessage.Message = "The other: " + message.message;
                    // echoMessage.Message = "Message"

                    // if it's not a private message, the echo message will be to the current user
                    if (!roomId && !conversationId)
                        echoMessage.UserToId = current_user_id;  // Id del usuario actual

                    // this will send a message to the user 1 (you) as if it was from user 2 (Echobot)
                    _this.clientAdapter.triggerMessagesChanged(echoMessage);
                     });
                // }, DemoAdapterConstants.ECHOBOT_REPLY_DELAY);
            });

   
        // }, DemoAdapterConstants.ECHOBOT_TYPING_DELAY);

    };

    DemoServerAdapter.prototype.sendTypingSignal = function (roomId, conversationId, userToId, done) {
        console.log("DemoServerAdapter: sendTypingSignal");
    };

    DemoServerAdapter.prototype.getMessageHistory = function (roomId, conversationId, otherUserId, done) {
        console.log("DemoServerAdapter: getMessageHistory");
        done([]);
    };

    DemoServerAdapter.prototype.getUserInfo = function (userId, done) {
        console.log("DemoServerAdapter: getUserInfo");
        var user = null;
        for (var i = 0; i < this.users.length; i++) {
            if (this.users[i].Id == userId) {
                user = this.users[i];
                break;
            }
        }
        if (user == null)
            throw "User doesn't exit. User id: " + userId;
        done(user);
    };

    DemoServerAdapter.prototype.getUserList = function (roomId, conversationId, done) {
        console.log("DemoServerAdapter: getUserList");
        if (roomId == DemoAdapterConstants.DEFAULT_ROOM_ID) {
            done(this.users);
            return;
        }
        throw "The given room or conversation is not supported by the demo adapter";
    };

    DemoServerAdapter.prototype.enterRoom = function (roomId, done) {
        console.log("DemoServerAdapter: enterRoom");

        if (roomId != DemoAdapterConstants.DEFAULT_ROOM_ID)
            throw "Only the default room is supported in the demo adapter";

        var userListChangedInfo = new ChatUserListChangedInfo();
        userListChangedInfo.RoomId = DemoAdapterConstants.DEFAULT_ROOM_ID;
        userListChangedInfo.UserList = this.users;

        this.clientAdapter.triggerUserListChanged(userListChangedInfo);
    };

    DemoServerAdapter.prototype.leaveRoom = function (roomId, done) {
        console.log("DemoServerAdapter: leaveRoom");
    };

    // gets the given user from the user list
    DemoServerAdapter.prototype.getUserById = function (userId) {
        for (var i = 0; i < this.users.length; i++) {
            if (this.users[i].Id == userId)
                return this.users[i];
        }
        throw "Could not find the given user";
    };
    return DemoServerAdapter;
})();

var DemoAdapter = (function () {
    function DemoAdapter() {
    }
    // called when the adapter is initialized
    DemoAdapter.prototype.init = function (done) {
        this.client = new DemoClientAdapter();
        this.server = new DemoServerAdapter(this.client);
        done();
    };
    return DemoAdapter;
})();
//# sourceMappingURL=jquery.chatjs.adapter.demo.js.map
