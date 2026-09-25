#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (!err) {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const film of results) {
      for (const character of film.characters) {
        if (character.includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
