#!/usr/bin/node
const { argv } = require('node:process');
function fact (num) {
  if (num === 0) {
    return (1);
  }
  return (num * fact(num - 1));
}
if (argv[2] === undefined) {
  console.log(1);
} else {
  console.log(fact(Number(argv[2])));
}
