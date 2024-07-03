#!/bin/bash

pushd "$(dirname "$(readlink -f "$0")")"
cd ../../implementation-provider
docker build -t implementation-provider:latest .
kind load docker-image implementation-provider:latest