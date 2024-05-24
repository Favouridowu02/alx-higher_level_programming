#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length <= 3) {
  console.log(0);
} else {
  let num = 0;
  let num2 = 0;
  for (let i = 2; i < argv.length; i++) {
    if (num <= Number(argv[i])) {
      num2 = num;
      num = Number(argv[i]);
    } else if (Number(argv[i]) > num2 && Number(argv[i]) < num) {
      num2 = Number(argv[i]);
    }
  }
  console.log(num2);
}
