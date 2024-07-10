#!/bin/bash

set -e

./build.sh

pushd distributor
dana -sp "../server;../constant" Distributor.o
