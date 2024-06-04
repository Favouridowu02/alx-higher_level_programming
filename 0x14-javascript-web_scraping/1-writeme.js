#!/usr/bin/node
const { writeFileSync } = require('fs');
const { argv } = require('node:process');
writeFileSync(argv[2].toString(), argv[3].toString(), { encoding: 'utf-8' });
