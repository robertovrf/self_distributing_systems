# Projeto Final de Graduação

## Para compilar o projeto:

Dê permissão para o arquivo "build.sh" executar:

$ chmod +x build.sh

Execute-o:

$ ./build.sh

## Para executar o servidor:

Entre na pasta __server__ em um terminal e digite:

$ dana main.o

Note: Não há a necessidade de executar o servidor desta forma se for executar o Distributor, seguindo as instruções abaixo.

## Para executar o distribuidor (local e remote):

Abra três terminais na pasta _distributor_. No primeiro execute:

$ dana -sp "../server;../readn" Distributor.o

Em um segundo terminal digite:

$ dana -sp ../readn RemoteDist.o

Em um terceiro terminal digite:

$ dana -sp ../readn RemoteDist.o 8082 2011

A primeira composição do servidor que o Distribuidor monta é a versão local. Para distribuí-lo, digite help e escolhar qual opção de distribuir. Para tornar o servidor todo local novamente, digite local.
