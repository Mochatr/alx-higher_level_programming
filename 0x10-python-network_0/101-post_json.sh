#!/bin/bash
#This script Sends a request to a URL passed as an argument, and displays only the status code of the response
curl -sX POST -H "content-type: application/json" -d "@$2" "$1"
