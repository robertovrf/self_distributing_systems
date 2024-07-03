#!/bin/bash

./scripts/bash/build-implementation-provider.sh
kubectl delete pod -l app=implementation-provider --wait=true

sleep 3
kubectl logs -l app=implementation-provider -f