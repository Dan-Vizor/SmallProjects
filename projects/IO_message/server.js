var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

var users = 0;

app.get('/', function(req, res){
  res.sendFile(__dirname + '/user.html');
});

io.on('connection', function(socket){
  socket.on('chat message', function(msg){
    io.emit('chat message', msg);
  });
});

io.on('connection', function(socket){
  users += 1;
  console.log("users online: " + users)
  socket.on('disconnect', function(){
    users -= 1;
    console.log("users online: " + users)
  });
});

http.listen(3000, function(){
  console.log('server listening on port: 3000');
});
