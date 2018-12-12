var express = require('express');
var http = require('http');
var path = require('path');
var app = express();
var port = 3000


app.use(express.static(path.join(__dirname, 'public')));

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});


http.createServer(app).listen(port, function(){
	console.log('server online on port: ' + port)
}); 
