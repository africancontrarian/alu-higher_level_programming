#!/bin/bash
# Sends a JSON POST request with a file's contents as the body, displays the response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
