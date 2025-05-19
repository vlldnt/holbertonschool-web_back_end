const http = require('http');

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Conteent-Type', 'text/plain');
  res.end('Hello Holberton School!');
});
app.listen(1245, '127.0.0.1');

module.exports = app;
