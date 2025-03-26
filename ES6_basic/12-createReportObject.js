export default function createReportObject(employeesList) {
  return {
    allEmployees: { ...employeesList },
    getNumberOfDepartments(employee) {
      return Object.keys(employee).lenght;
    },
  };
}
