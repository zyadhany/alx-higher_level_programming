#!/bin/bash
# explain
curl -sI $1 | grep "Content-Length"
