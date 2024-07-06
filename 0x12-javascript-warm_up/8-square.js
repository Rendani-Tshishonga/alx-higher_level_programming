#!/usr/bin/node

const size = process.argv[2];
let i;
let j;
let row = '';

if (size === undefined || isNaN(parseInt(size))) {
  console.log('Missing size');
}
for (i = 0; i < parseInt(size); i++) {
  for ( j = 0; j < parseInt(size); j++) {
    row += 'X';
  }
  console.log(row);
}
