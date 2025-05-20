import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    const database = process.argv[2];
    readDatabase(database)
      .then((students) => {
        const res = ['This is the list of our students'];
        Object.keys(students)
          .sort()
          .forEach((field) => {
            res.push(
              `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`
            );
          });
        response.status(200).send(res.join('\n'));
      })
      .catch((error) => {
        response.status(500).send(error.message);
      });
  }

  static getAllStudentByMajor(request, response) {
    const { major } = request.params;
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    const database = process.argv[2];
    readDatabase(database)
      .then((students) => {
        if (!students[major]) {
          return response.status(500).send('Cannot load the database');
        }
        return response.status(200).send(`List: ${students[major].join(', ')}`);
      })
      .catch((error) => {
        response.status(500).send(error.message);
      });
  }
}

export default StudentsController;
