#!/usr/bin/node
const argv = process.argv;
const firstNumber = parseInt(argv[2]);
const secondNumber = parseInt(argv[3]);

function add (a, b) {
  return (a + b);
}

console.log(add(firstNumber, secondNumber));
