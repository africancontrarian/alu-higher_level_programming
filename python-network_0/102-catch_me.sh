#!/bin/bash
# Requests 0.0.0.0:5000/catch_me and lets curl print the response body itself
curl -s -X GET "0.0.0.0:5000/catch_me"
