export default function getStudentsByLocation(studentsList, city) {
  return studentsList.filter((name) => name.location === city);
}
