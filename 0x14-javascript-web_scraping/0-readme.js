#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
const nameFile = argv[2];
fs.readFile(nameFile, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  process.stdout.write(data);
});
