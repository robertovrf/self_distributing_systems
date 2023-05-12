#!/bin/bash

echo ":::Compiling Server:::"
cd server
dnc . -v
echo ":::Compiling Distributor:::"
cd ../distributor
dnc . -sp ../server -v
echo ":::Compiling list constant:::"
cd ../constant/data/adt
dnc . -v
echo ":::Compiling list readn:::"
cd ../../../readn/data/adt
dnc . -v
echo ":::Compiling list readn-writen:::"
cd ../../../readn-writen/data/adt
dnc . -v
echo ":::Compiling list writen:::"
cd ../../../writen/data/adt
dnc . -v
echo ":::Compiling Client:::"
cd ../../../client
dnc . -v

