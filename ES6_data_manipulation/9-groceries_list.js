
export default function groceriesList() {
    const names = ['Apples', 'Tomatoes', 'Pasta', 'Rice', 'Banana'];
    const quantities = [10, 10, 1, 1, 5];
    const My_list = new Map()

    for (let i = 0; i < name.length; i += 1){
        My_list.set(names[i], quantities[i]);
    }

    return My_list;
}