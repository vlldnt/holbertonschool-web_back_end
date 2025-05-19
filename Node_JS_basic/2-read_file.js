const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter((line) => line);
    const fields = {};
    const students = lines.slice(1);

    students.forEach((line) => {
      const student = line.split(',');
      const field = student[3];
      if (!fields[field]) fields[field] = [];
      fields[field].push(student[0]);
    });

    console.log(`Number of students: ${students.length}`);
    for (const field in fields) {
      if (field) {
        const list = fields[field].join(', ');
        console.log(
          `Number of students in ${field}: ${fields[field].length}. List: ${list}`
        );
      }
    }
  } catch (error) {
    throw Error('Cannot load the database');
  }
}

module.exports = countStudents;
