#!/usr/local/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(body.title);
  }
});
