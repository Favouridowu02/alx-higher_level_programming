#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');
const uri = argv[2];
request(uri, { json: true }, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  let number = 0;
  const count = Number(body.count);
  for (let i = 0; i < count; i++) {
    if (body.results[i].characters.toString().includes('18')) {
      number++;
    }
  }
  console.log(number);
});
