#!/usr/bin/node
const { argv } = require('node:process');
const len = argv.length;
if (len === 2) {
  console.log('No argument');
} else {
  for (let i = 1; i < len; i++) {
    console.log(argv[i]);
  }
}
