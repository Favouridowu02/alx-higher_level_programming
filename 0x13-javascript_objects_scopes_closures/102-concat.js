#!/usr/bin/node
const { readFileSync, writeFileSync } = require('fs');
const first = readFileSync(process.argv[2].toString());
const second = readFileSync(process.argv[3].toString());
writeFileSync(process.argv[4], first + second);
