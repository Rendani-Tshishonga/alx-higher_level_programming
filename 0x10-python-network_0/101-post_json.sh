#!/bin/bash
# A script to send a JSON POST request
curl -sX POST "$1" -d @"$2"
