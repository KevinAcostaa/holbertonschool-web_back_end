export default function groceriesList() {
  const names = ['Apples', 'Tomatoes', 'Pasta', 'Rice', 'Banana'];
  const quantities = [10, 10, 1, 1, 5];
  const mylist = new Map();

  for (let i = 0; i < names.length; i += 1) {
    mylist.set(names[i], quantities[i]);
  }

  return mylist;
}
