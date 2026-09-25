#!/usr/bin/node
const request = require('request');
request('https://jsonplaceholder.typicode.com/todos', (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    const completed = {};
    for (const todo of todos) {
      if (todo.completed === true) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1;
        } else {
          completed[todo.userId]++;
        }
      }
    }
    console.log(completed);
  }
});
