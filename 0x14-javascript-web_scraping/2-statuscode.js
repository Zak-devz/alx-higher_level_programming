#!/usr/bin/node
const request = require('request');

let url = process.argv[2];

request(url, (response) => {
  console.log(`code: ${response.statusCode}`);
});
