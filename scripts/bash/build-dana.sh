#!/bin/bash

pushd "$(dirname "$(readlink -f "$0")")"
docker build -t dana:253 -f ../docker/dana/Dockerfile .
kind load docker-image dana:253