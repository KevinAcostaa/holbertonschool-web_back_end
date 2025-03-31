
class HolbertonCourse {
    constructor(name, lenght, students) {
        if (typeof name != 'string') {
            throw new TypeError('Name must be a string');
        }
        if (typeof lenght != 'number') {
            throw new TypeError('Lenght must be a number');
        }
        if (!Array.isArray(students) || !students.every((student) => typeof student === 'string')) {
            throw new TypeError('Students must be an array of strings');
        }

        this._name = name;
        this._lenght = lenght;
        this._students = students;
    }

    get name() {
        return this._name;
    }

    set name(value) {
        if (typeof value != 'string') {
            throw new TypeError('students must be an array of string')
        }
        this._name = value;
    }

    get length() {
        return this._length;
    }

    set length(value) {
        if (typeof value !== 'number') {
            throw new TypeError('length must be a number');
        }
        this._length = value;
    }

    get students() {
        return this._students;
    }

    set students(value) {
        if (!Array.isArray(value) || !value.every((student) => typeof student === 'string')) {
            throw new TypeError('students must be an array of strings');
        }
        this._students = value;
    }
}

export default HolbertonCourse;