#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');
const uri = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];
request(uri, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const main = JSON.parse(body);
  main.characters.forEach((item) => {
    request(item, function (error, response, content) {
      if (error) {
        console.error(error);
        return;
      }
      const def = JSON.parse(content);
      console.log(def.name);
    });
  });
});
