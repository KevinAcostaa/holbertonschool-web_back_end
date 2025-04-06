export default function updateStudentGradeByCity(students, city, newGrades) {
    const newList = students.filter((student) => student.location === city);
    const list_update = newList.map((student) => {
        const new_grade = newGrades.find((grade) => grade.studentId === student.id);
        return {
            ...student,
            grade: new_grade ? new_grade.grade : 'N/A',
        };
    });


    return list_update;
}