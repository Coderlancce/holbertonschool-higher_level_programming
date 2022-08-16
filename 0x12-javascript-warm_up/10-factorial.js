#!/usr/bin/node
const argv = process.argv;
const number = parseInt(argv[2]);

function factorial (a) {
  if (isNaN(a)) {
    return (1);
  }
  if (a === 0) {
    return (1);
  }
  return (a * factorial(a - 1));
}

console.log(factorial(number));
