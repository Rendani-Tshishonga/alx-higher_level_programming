#!/usr/bin/node
// A Script that updates the text color
// of a header with id attribute of #DIVheader

$('div#red_header').click(function (){
	$('header').css('color', '#FF0000');
});
