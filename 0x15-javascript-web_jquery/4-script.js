#!/usr/bin/node
// A Script that toggles the class of the header

$('DIV#toggleheader').click(function ()
{
	if $('header').hasClass('red')
		$('header').addClass('green');
	else
		$('header').addClass('red');
});
