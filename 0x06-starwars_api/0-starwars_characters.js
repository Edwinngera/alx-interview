#!/usr/bin/node
// script that prints all characters of a Star Wars movie in order
const request = require('request');
const myArgs = process.argv.splice(2);
const URL = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
request.get(URL, async (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const character = JSON.parse(body).characters;
    const characterList = characterURLs => {
      const promise = new Promise((resolve, reject) => {
        request.get(characterURLs, (err, response, body) => {
          if (err) {
            reject(err);
          } else {
            resolve(body);
          }
        });
      });
      return promise;
    };
    for (let i = 0; i < character.length; i++) {
      const result = await characterList(character[i]);
      console.log(JSON.parse(result).name);
    }
  }
});