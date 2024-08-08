#!/usr/bin/node
// A Script that adds an element
// to a list.

$('DIV#add_item').click(function ()
{
	const element = "<li>Item</li>";

	$('UL.my_list').append(element);
}
