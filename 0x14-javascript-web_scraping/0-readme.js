#!/usr/bin/node
const fs = require('fs');
const content = fs.readFileSync(process.argv[2], { encoding: 'utf-8' });
console.log(content);
