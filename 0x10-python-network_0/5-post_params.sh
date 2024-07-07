#!/bin/bash
# A script that sends a POST reuest to the passed URL
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
