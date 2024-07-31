#!/usr/bin/node
/*
 * A script that prints the number of movies
 * where the character "Wedge Antilles" is.
 */

const request = require('request');
let num = 0;

request.get(process.argv[2], function (error, response, body) {
	if (error) {
		console.error(error);
	}
	const content = JSON.parse(body);
	content.results.forEach((film) => {
		film.characters.forEach((character) => {
			if (character.includes(18)) {
				num += 1;
			}
		});
	});
	console.log(num);
});
