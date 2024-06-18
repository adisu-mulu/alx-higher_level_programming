#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length - 2 === 0) {
  console.log('No argument');
} else if (argv.length - 2 === 1) {
  console.log(argv[2]);
} else {
  console.log('Arguments found');
}
