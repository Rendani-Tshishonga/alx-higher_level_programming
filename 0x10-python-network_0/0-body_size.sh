#!/bin/bash
# A bash script that takes in a URL, request the URL and counts the number of bytes
curl -s "$1" | wc -c
