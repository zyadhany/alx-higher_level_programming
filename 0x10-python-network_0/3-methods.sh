#!/bin/bash
# explain
curl -sI ALLOW $1 | grep "ALLOW"
