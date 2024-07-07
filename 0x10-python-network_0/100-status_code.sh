#!/bin/bash
# A script to display the status code of a response
curl -s --head "$1" | awk '/^HTTP/{print $2}'
