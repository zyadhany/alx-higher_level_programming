#!/bin/bash
# explain
curl -sI ALLOW $1 | grep "Allow" | cut -d " " -f2-
