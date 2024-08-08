#!/usr/bin/node
// A Script that updates the text of a header

$('DIV#update_header').click(function ()
{
	$('header').text('New Header!!!');
});
