var express = require('express');
var http = require('http');
var path = require('path');
var mongodb = require('mongodb');
var bodyParser  = require('body-parser');
var app = express();
var server = new mongodb.Server('127.0.0.1', 27017, {});
var client = new mongodb.Db('Solar', server, {w: 1});

app.use(express.static(path.join(__dirname, 'public'))); 
app.use(bodyParser.json());
app.get('/', function(req, res) {
	res.send('');
});

app.get('/planets', function(req, res) {
	var planets = [];
	res.setHeader('Content-Type', 'application/json');
	client.open(function(err) {
		if (err) console.log('error opening collection', err);
		client.collection('planets', function(err, collection) {
			if (err) console.log('error reading collection', err);
			collection.find().toArray(
				function(err, results) {
					if (err) console.log('error finding planets', err);
					console.log('page loaded');
					console.log('planets found', results);
					console.log('');
					planets = results;
					res.send(results);
					client.close();
				});
		});
	});
		
});
app.put('/planet', function(req, res) {
	console.log(req.body)
	client.open(function(err) {
		client.collection('planets', function(err, collection) {
			if (err) console.log('error opening collection:', err);
			collection.insert(req.body, function(err, data) {
				if (err) {
					console.log('error')
				}
				console.log('planet inserted')
			res.send('ok');
			client.close();
			});
		
	})
});
});

http.createServer(app).listen(3000, function(){
	console.log('server on')
}); 