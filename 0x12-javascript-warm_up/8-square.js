#!/usr/bin/node
const { argv } = require('node:process');
const length = argv[2];
if (argv[2] === undefined || isNaN(argv[2]) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < length; i++) {
    for (let j = 0; j < length; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
