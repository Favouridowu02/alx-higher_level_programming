#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');
const uri = 'https://jsonplaceholder.typicode.com/todos';
request(uri, (error, response, body) => {
  if (error) {
    return error;
  }
  const newObj = {};
  const todos = JSON.parse(body);
  const count = body.length;
  todos.forEach((todo) => {
    if (todo.completed && newObj[todo.userId] === undefined) {
      newObj[todo.userId] = 1;
    } else if (newObj[todo.userId]) {
      newObj[todo.userId] += 1;
    }
  });
  console.log(newObj);
});
