#!/bin/bash

set -e

pushd "$(dirname "$(readlink -f "$0")")"
cd ../../
docker build -t remote-dist:all -f scripts/docker/remote_dist/Dockerfile .
docker tag remote-dist:all robertovrf/remote-dist:all
kind load docker-image robertovrf/remote-dist:all