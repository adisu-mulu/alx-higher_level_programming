#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] === undefined || isNaN(Number(argv[2]))) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < Number(argv[2])) {
    let j = 0;
    let str = '';
    while (j < Number(argv[2])) {
      str = str + 'X';
      j++;
    }
    console.log(str);
    i++;
  }
}
