export default function getStudentIdsSum(students) {
  const ids = students.map((students) => students.id);
  return ids.reduce(
    (accumulator, currentValue) => accumulator + currentValue, 0,
  );
}
