#!/usr/bin/node
const { writeFileSync } = require('fs');
const argv = require('node:process').argv;
writeFileSync(argv[2].toString(), argv[3] + '\n', { encoding: 'utf-8' });
