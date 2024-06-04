#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');
const uri = 'https://jsonplaceholder.typicode.com/todos';
request(uri, (error, response, body) => {
  if (error) {
    return error;
  }
  const newObj = {};
  body = JSON.parse(body);
  const count = body.length;
  for (let i = 0; i < count; i++) {
    let id = body[i].userId;
    if (body[i].completed === true) {
      if (!newObj[id]) {
        newObj[id] = 1;
      } else {
        newObj[id] += 1;
      }
    }
  }
  console.log(newObj);
});
