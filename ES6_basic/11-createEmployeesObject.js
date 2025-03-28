export default function createEmployeesObject(departmentName, employees) {
    const depart = {
        [departmentName.toLowerCase()]: employees,
    };
    return depart;
}