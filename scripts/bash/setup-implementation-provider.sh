#!/bin/bash

set -e

pushd "$(dirname "$(readlink -f "$0")")"
kubectl delete --ignore-not-found=true -f ../kubernetes/implementation-provider/

kubectl apply -f ../kubernetes/rbac 
kubectl apply -R -f ../kubernetes/implementation-provider/
