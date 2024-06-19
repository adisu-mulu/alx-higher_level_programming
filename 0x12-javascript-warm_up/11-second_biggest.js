#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] === undefined || argv[3] === undefined) {
  console.log(0);
} else {
  let biggest = Number(argv[2]);
  for (let i = 3; i < argv.length; i++) {
    if (Number(argv[i]) > biggest) {
      biggest = argv[i];
    }
  }
  console.log(biggest);
}
