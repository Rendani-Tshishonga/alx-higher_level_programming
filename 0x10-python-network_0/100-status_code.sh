#!/bin/bash
# A script to display the status code of a response
curl -s --output /dev/null --write-out "%{http_code}" "$1"
