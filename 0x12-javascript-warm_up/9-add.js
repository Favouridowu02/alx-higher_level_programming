#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(argv[2])|| isNaN(argv[3])) {
  console.log("NaN");
} else {
  console.log(Number(argv[2]) + Number(argv[3]));
}
