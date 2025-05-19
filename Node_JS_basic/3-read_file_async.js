// the function will read database.csv but it's async this time !

const fs = require('fs');

const countStudents = async (filecsv) => {
  let csv = '';

  try {
    csv = await fs.readFileSync(filecsv, 'utf-8');
  } catch (err) {
    throw new Error('cannot load the database');
  }

  const datacsv = csv.split('\n').slice(1);
  const data = datacsv
    .map((line) => line.split(','))
    .filter((student) => student.length === 4);

  const studentData = data.map((student) => ({
    firstname: student[0],
    lastname: student[1],
    age: student[2],
    field: student[3],
  }));

  const studentCS = studentData
    .filter((data) => data.field === 'CS')
    .map((map) => map.firstname);
  const studentSWE = studentData
    .filter((data) => data.field === 'SWE')
    .map((map) => map.firstname);

  console.log(`Number of students: ${studentData.length}`);
  console.log(
    `Number of students in CS: ${studentCS.length}. List: ${studentCS.join(', ')}`
  );
  console.log(
    `Number of students in SWE: ${studentSWE.length}. List: ${studentSWE.join(', ')}`
  );

  return { studentData, studentCS, studentSWE };
};

module.exports = countStudents;
