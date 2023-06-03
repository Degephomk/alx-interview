#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Define the API URL
const API_URL = 'https://swapi-api.hbtn.io/api';

// Check if the movie ID argument is provided
if (process.argv.length > 2) {
  // Make a request to retrieve the movie data
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }

    // Parse the movie data and extract the character URLs
    const charactersURL = JSON.parse(body).characters;

    // Map each character URL to a Promise that fetches the character data
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        // Make a request to fetch the character data
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          // Resolve the Promise with the character name
          resolve(JSON.parse(charactersReqBody).name);
        });
      })
    );

    // Wait for all character Promises to resolve
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n'))) // Print all the character names
      .catch(allErr => console.log(allErr)); // Handle any errors during Promise execution
  });
}
