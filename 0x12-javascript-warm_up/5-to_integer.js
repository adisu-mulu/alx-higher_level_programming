#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] === undefined || isNaN(Number(argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(argv[2]));
}
