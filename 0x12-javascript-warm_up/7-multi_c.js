#!/usr/bin/node
const arg = process.argv[2];

if (!arg || isNaN(arg) || parseInt(arg) <= 0) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < parseInt(arg); i++) {
    console.log('C is fun');
  }
}
