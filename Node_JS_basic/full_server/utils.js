import fs from 'fs';

export default function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim());
      const [header, ...entries] = lines;
      const headers = header.split(',');

      const students = entries.map((line) => {
        const values = line.split(',');
        return headers.reduce((obj, key, i) => {
          obj[key] = values[i];
          return obj;
        }, {});
      });

      const grouped = {};
      for (const student of students) {
        const field = student.field;
        if (!grouped[field]) grouped[field] = [];
        grouped[field].push(student.firstname);
      }

      resolve(grouped);
    });
  });
}
