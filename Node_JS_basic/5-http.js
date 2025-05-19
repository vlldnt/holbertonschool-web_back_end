// this function will a small http server with the module Node HTTP

const httpServer = require('http');
const countStudents = require('./3-read_file_async');

const host = '127.0.0.1';
const port = 1245;
const database = process.argv[2];

const app = httpServer.createServer(async (req, res) => {
  if (req.url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const { studentData, studentCS, studentSWE } =
        await countStudents(database);
      res.write(`Number of students: ${studentData.length}\n`);
      res.write(
        `Number of students in CS: ${studentCS.length}. List: ${studentCS.join(', ')}\n`
      );
      res.write(
        `Number of students in SWE: ${studentSWE.length}. List: ${studentSWE.join(', ')}`
      );
      res.end();
    } catch (error) {
      res.end(error.message);
    }
  } else {
    res.statusCode = 404;
    res.end('Invalid request');
  }
});

app.listen(port, host);
module.exports = app;
