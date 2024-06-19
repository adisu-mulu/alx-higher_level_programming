#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] === undefined || argv[3] === undefined) {
  console.log(0);
} else {
  let biggest = Number(argv[2]);
  for (let i = 3; i < argv.length; i++) {
    if (Number(argv[i]) > biggest) {
      biggest = Number(argv[i]);
    }
  }
  let j, second;
  if (Number(argv[2]) === biggest) {
    second = argv[3];
    j = 4;
  } else {
    second = argv[2];
    j = 3;
  }
  while (j < argv.length) {
    if (Number(argv[j]) > second && Number(argv[j]) < biggest) {
      second = Number(argv[j]);
      j++;
    } else {
      j++;
    }
  }
  console.log(second);
}
