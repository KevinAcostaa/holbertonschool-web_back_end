export default function createReportObject(employeesList) {
    const My_list = {
        allEmployees: {
            ...employeesList,
        },
        getNumberOfDepartments: () => Object.keys(employeesList).length,
    };
    return My_list;
}