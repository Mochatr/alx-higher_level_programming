#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(args[2], (error, response, body) => {
	if (!error) {
		let movies = 0;
		const moviesData = JSON.parse(body).results;

		moviesData.forEach(character) => {
			movie.characters.forEach((character) => {
				if (character.endsWith('/18/')) movies++;
			});
		});
		
		console.log(movies);
	}
});
