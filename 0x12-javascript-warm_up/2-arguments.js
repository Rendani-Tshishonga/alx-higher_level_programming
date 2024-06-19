#!/usr/bin/node
const arg = process.argv;

if (arg.length <= 2){
  console.log('No Arguments');
} else if (arg.length === 3){
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
