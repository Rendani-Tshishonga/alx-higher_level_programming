#!/usr/bin/node

const x = process.argv[2];
let i = 0;

if (x === undefined) {
  console.log('Missing number of occurences');
}
while (i < x) {
  console.log('C is fun');
  i++;
}
