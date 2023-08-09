#!/usr/bin/node
/*
 * This script expects a StarWars movie ID and returns all other
 * characters in that movie
 */
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, data) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(data).characters;
    printName(characters, 0);
  }
});
/**
 * printName - prints a name of all characters in the array
 * @array: an array of items
 * @index: the starting index
 */
function printName (array, index) {
  request(array[index], (err, resp, data) => {
    if (!err && resp.statusCode === 200) {
      const character = JSON.parse(data);
      console.log(character.name);
    }
    if (index < array.length - 1) {
      printName(array, index + 1);
    }
  });
}
