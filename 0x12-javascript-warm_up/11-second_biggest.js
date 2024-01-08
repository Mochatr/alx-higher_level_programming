#!/usr/bin/node

let max = 0;
let secondMax = 0;

for (let i = 2; i < process.argv.length; i++) {
  const num = parseInt(process.argv[i]);

  if (num > max) {
    secondMax = max;
    max = num;
  } else if (num > secondMax) {
    secondMax = num;
  }
}

if (process.argv.length <= 2) {
  console.log(0);
} else {
  console.log(secondMax);
}
