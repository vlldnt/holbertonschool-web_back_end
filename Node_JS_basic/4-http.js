var http = require("http");

http.createServer(function(req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write("Hello Holberton School!");
  res.end();
}).listen(1245);

module.exports = app;