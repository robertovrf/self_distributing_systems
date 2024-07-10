#!/bin/bash

set -e

./scripts/bash/build-remote-dist.sh
./scripts/bash/build-implementation-provider.sh
./scripts/bash/setup-implementation-provider.sh
kubectl delete pod -l app=implementation-provider --wait=true

sleep 3
kubectl logs -l app=implementation-provider -f