#!/usr/bin/node
// A script that prints a Star Wars title
// by giving the espisode

const request = require('request');
const url = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];

request(url, function (error, response, body) {
	if (error) {
		console.error(error);
	}
	const content = JSON.parse(body);
	console.log(content.title);
});
