#!/usr/bin/node
const addMeMaybe = function (number, theFunction) {
  const x = number + 1;
  theFunction(x);
};
exports.addMeMaybe = addMeMaybe;
