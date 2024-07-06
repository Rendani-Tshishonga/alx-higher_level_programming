#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];

function add (a, b) {
  return a + b;
}

const arg1 = parseInt(a);
const arg2 = parseInt(b);
console.log(add(arg1, arg2));
