#!/bin/bash
# Write a bash script that takes in a URL and displays all HTTP methods the server will accept
curl -sIX HEAD "$1"
