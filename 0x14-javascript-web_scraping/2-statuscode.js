#!/usr/local/bin/node
const request = require('request');

let url = process.argv[2];

request(url, (err, response) => {
  if (err) {
    console.log(err);
  }
  console.log(`code: ${response.statusCode}`);
});
