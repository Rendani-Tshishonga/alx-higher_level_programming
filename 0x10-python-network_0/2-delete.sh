#!/bin/bash
# Write a bash script that sends a DELETE request to the URL and returns the body of the request
curl -s -X DELETE "$1"
