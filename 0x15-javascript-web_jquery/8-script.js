#!/usr/bin/node
// A script that fetches and lists the title
// of the movie in HTML

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function(data)
{	
	const movies = data.results;
	for (let movie of movies) {
		$('UL#list_movies').append(`<li>${movie.title}</li>`);
	}
});
