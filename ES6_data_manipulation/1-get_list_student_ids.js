export default function getListStudentsIds(studentsList) {
  if (!Array.isArray(studentsList)) return [];
  return studentsList.map((studentsList) => studentsList.id);
}
