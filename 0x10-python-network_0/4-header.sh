#!/bin/bash
#pass a variable in the header of the request
curl -s "$1" -X GET -H "X-School-User-Id: 98"
