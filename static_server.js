var connect = require('connect'),
    serveStatic = require('serve-static'),
    directory = "/home/SIAV/app/static"

var app = connect();

//CORS middleware
var allowCrossDomain = function(req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

    next();
}
app.use(allowCrossDomain);
app.use(serveStatic(directory));
app.listen(8000);
console.log('Listening on port 8000.');
