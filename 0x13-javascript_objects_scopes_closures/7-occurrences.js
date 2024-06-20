#!/usr/bin/node

exports.nbOccurences = function (list, SearchElement) {
  let i;
  let count = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === SearchElement) {
      count++;
    }
  }
  return count;
};
