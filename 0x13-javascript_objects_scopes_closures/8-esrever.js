#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  let j;

  while ((len - i) > 0) {
    j = list[len];
    list[len] = list[i];
    list[i] = j;
    i++;
    len--;
  }
  return list;
};
