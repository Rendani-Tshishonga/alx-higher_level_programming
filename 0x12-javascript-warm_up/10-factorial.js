#!/usr/bin/node

let arg1 = process.argv[2];

if (isNaN(parseInt(arg1))) {
  arg1 = 1;
}
function factorial (n) {
  if (n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(arg1));
