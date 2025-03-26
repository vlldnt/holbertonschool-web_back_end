export default function createReportObject(employeesList) {
    return {
        allEmployees: { ...employeesList } ,
        getNumberOfDepartments(empl) {
            return Object.keys(empl).lenght;
        }
    };
}