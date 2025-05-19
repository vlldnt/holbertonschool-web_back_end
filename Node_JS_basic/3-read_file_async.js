const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data.split('\n').filter((line) => line.length > 0);
      if (lines.length <= 1) {
        resolve('Number of students: 0');
        return;
      }

      const fields = {};
      for (let i = 1; i < lines.length; i += 1) {
        const student = lines[i].split(',');
        if (fields[student[3]]) {
          fields[student[3]].push(student[0]);
        } else {
          fields[student[3]] = [student[0]];
        }
      }

      let output = `Number of students: ${lines.length - 1}`;
      for (const field in fields) {
        if (field) {
          const list = fields[field];
          output += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
        }
      }

      resolve(output);
    });
  });
}

module.exports = countStudents;