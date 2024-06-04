#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');
const uri = argv[2];
const { writeFileSync } = require('fs');
request(uri, (error, response, body) => {
  if (error) {
    return error;
  }
  writeFileSync(argv[3].toString(), body, { encoding: 'utf-8' });
});
