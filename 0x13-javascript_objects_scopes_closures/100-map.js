#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map((num, index) => {
  return (num * index);
});
console.log(list);
console.log(newList);
