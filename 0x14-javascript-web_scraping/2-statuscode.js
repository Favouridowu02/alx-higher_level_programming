#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');
request
  .get(argv[2])
  .on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
  });
