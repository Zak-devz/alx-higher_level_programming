#!/usr/local/bin/node
const request = require('request');

const url = process.argv[2];
const characterId = '18';

request(url, (err, res, body) => {
  if (!err) {
    const data = JSON.parse(body);
    const count = data.results.reduce((count, movie) => {
      return movie.characters.find((character) =>
        character.endsWith(`/${characterId}/`)
      )
        ? count + 1
        : count;
    }, 0);
    console.log(`${count}`);
  }
});
