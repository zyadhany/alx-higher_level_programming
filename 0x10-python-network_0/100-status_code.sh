#!/bin/bash
# explain
curl -o ./tmp -sw "%{http_code}" $1
