#!/bin/bash
set -e

echo ":::Compiling Server:::"
pushd server
dnc . -v
popd
echo ":::Compiling list constant:::"
pushd constant/data/adt
dnc . -v
popd
echo ":::Compiling Distributor:::"
pushd distributor
dnc . -sp ../server -v
popd
echo ":::Compiling list readn:::"
pushd readn/data/adt
dnc . -v
popd
echo ":::Compiling list readn-writen:::"
pushd readn-writen/data/adt
dnc . -v
popd
echo ":::Compiling list writen:::"
pushd writen/data/adt
dnc . -v
popd
echo ":::Compiling Client:::"
pushd client
dnc . -v
popd

