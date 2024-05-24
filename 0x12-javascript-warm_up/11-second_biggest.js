#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] === undefined || isNaN(argv[2]) === true) {
  console.log(0);
} else {
  let num = 0;
  let num2 = 0;
  for (let i = 2; i <= argv.length; i++) {
    if (num < argv[i]) {
      num2 = num;
      num = argv[i];
    }
  }
  console.log(num2);
}
