var express = require('express');
var http = require('http');
var path = require('path');
var bodyParser  = require('body-parser');
var app = express();

app.use(express.static(path.join(__dirname, 'public'))); 
app.use(bodyParser.json());
app.get('/', function(req, res) {
	res.send('200');
});

http.createServer(app).listen(3000, function(){
	console.log('server online')
}); 
