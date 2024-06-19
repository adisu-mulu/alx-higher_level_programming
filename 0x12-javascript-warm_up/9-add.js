#!/usr/bin/node
const { argv } = require('node:process');
function add (a, b) {
  console.log(a + b);
}
if (argv[2] === undefined || argv[3] === undefined) {
  console.log('NaN');
} else {
  add(Number(argv[2]), Number(argv[3]));
}
