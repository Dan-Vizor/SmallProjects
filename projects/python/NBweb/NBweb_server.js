var app = require('express')();
var http = require('http').Server(app);
var path = require('path');

//app.use(app.static(path.join(__dirname, 'public')));
app.get('/', function(req, res){
  res.sendFile(__dirname + '/public/index.html');
  console.log('conection from: ' + request.connection.remoteAddress)
});

http.listen(3000, function(){
  console.log('server online and listening on port: 3000');
});
