const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const database = process.argv[2];
  countStudents(database)
    .then((output) => {
      res.set('Content-Type', 'text/plain');
      res.send(`This is the list of our students\n${output}`);
    })
    .catch((error) => {
      res.set('Content-Type', 'text/plain');
      res.send(`This is the list of our students\n${error.message}`);
    });
});

app.listen(1245);

module.exports = app;
