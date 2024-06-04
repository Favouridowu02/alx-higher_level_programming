#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');
const uri = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];
request(uri, { json: true }, function (error, response, body) {
  if (error) {
    console.erroor(error);
  }
  console.log(body.title);
});
