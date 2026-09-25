#!/usr/bin/node
const n = Math.floor(Number(process.argv[2]));
if (isNaN(n)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + n);
}
