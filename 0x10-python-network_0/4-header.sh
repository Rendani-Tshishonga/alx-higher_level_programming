#!/bin/bash
# A bash script that takes in a header variable with value and returns the HTTP reponse
curl -sH "X-School-User-Id: 98" "$1"
