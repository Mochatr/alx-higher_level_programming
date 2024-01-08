#!/usr/bin/node
const size = process.argv[2];

if (!size || isNaN(size) || parseInt(size) <= 0) {
  console.log('Missing size');
} else {
  const squareSize = parseInt(size);
  for (let i = 0; i < squareSize; i++) {
    console.log('X'.repeat(squareSize));
  }
}
