#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, response, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (err, response, body) => {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
