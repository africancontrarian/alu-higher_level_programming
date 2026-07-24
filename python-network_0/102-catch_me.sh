#!/bin/bash
# Requests 0.0.0.0:5000/catch_me and lets curl print the response body itself
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" "0.0.0.0:5000/catch_me"
