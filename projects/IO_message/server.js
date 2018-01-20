var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

var users = 0;
var log = {};

app.get('/', function(req, res){
  res.sendFile(__dirname + '/user.html');
});

io.on('connection', function(socket){
  socket.on('chat message', function(msg){
    io.emit('chat message', msg);
    log += msg;
  });
});

io.on('connection', function(socket){
  users += 1;
  console.log("users online: " + users)
  socket.on('chat message', function(msg){
	io.emit('chat message', "user connected");
  });
  socket.on('disconnect', function(){
    users -= 1;
    socket.on('chat message', function(msg){
	io.emit('chat message', "user disconnected");
  });
    console.log("users online: " + users)
  });
});

http.listen(3000, function(){
  console.log('server listening on port: 3000');
});
