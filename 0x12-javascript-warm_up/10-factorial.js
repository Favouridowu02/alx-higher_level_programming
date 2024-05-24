#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] === undefined || isNaN(argv[2]) === true) {
  console.log(1);
} else {
  function fact (num) {
    if (num === 1 || num === 0) {
      return (1);
    }
    return (num * fact(num - 1));
  }
  console.log(fact(argv[2]));
}
