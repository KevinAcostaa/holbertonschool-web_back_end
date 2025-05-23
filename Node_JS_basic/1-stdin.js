const Myline = require('readline');

const Ml = Myline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

Ml.question('Welcome to Holberton School, what is your name?\n', (name) => {
  console.log(`Your name is: ${name}`);
  console.log('This important software is now closing');
  Ml.close();
});
