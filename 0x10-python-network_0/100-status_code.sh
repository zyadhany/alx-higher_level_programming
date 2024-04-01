#!/bin/bash
# explain
curl -sw "%{http_code}" $1
