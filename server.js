var express = require('express');
var morgan = require('morgan');

var app = express();
var port = process.env.PORT || 8080;
var bodyParser = require('body-parser');
var router = express.Router();
var path = require('path');

app.use(morgan('dev'));
app.use(bodyParser.json()); // for parsing application/json
app.use(bodyParser.urlencoded({
  extended: true
})); // for parsing application/x-www-form-urlencoded

app.use(express.static(__dirname + '/public')); // GET /style.css etc
app.get('*', function (req, res) {
  res.sendFile(path.join(__dirname + '/public/app/views/index.html'));
});

app.listen(port, function () {
  console.log('Listening on port 8080');
});