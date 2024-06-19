#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  let i = 0;
  while (i < Number(argv[2])) {
    console.log('C is fun');
    i++;
  }
}
