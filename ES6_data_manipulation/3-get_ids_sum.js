export default function getStudentIdsSum(students) {
  const ids = students.map((students) => students.id);
  const startValue = 0;
  return ids.reduce(
    (accumulator, currentValue) => accumulator + currentValue, startValue,
  );
}
