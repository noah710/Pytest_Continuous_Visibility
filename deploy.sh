#!/bin/bash

docker build --no-cache -t ohs_cv_srv:latest .
docker run -d ohs_cv_srv:latest
