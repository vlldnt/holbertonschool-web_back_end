import express from 'express';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

const routes = express.Router();

routes.get('/', AppController.getHomepage);
routes.get('/students', StudentsController.getAllStudents);
routes.get('/students/:major', StudentsController.getAllStudentsByMajor);

export default routes;
