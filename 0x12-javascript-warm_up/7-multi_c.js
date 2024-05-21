#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] === undefined) {
  console.log('Missing number of occurrences')
} else if (isNaN(argv[2]) === false) {
  const lineNumber = argv[2];
  for (let i = 0; i < lineNumber; i++) {
    console.log('C is fun');
  }
}
