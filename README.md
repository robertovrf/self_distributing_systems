# Projeto Final de Graduação

## Para compilar o projeto:

### Servidor

Entre na pasta _server_ em um terminal e digite:

$ dnc . -v

### Distribuidor

Entre na pasta _distributor_ em um terminal e digite:

$ dnc . -v


### Cliente

Entre na pasta _client_ em um terminal e digite:

$ dnc . -v


## Para executar o servidor:

Entre na pasta __server__ em um terminal e digite:

$ dana main.o

## Para executar o distribuidor:

Abra três terminais na pasta _distributor_. No primeiro execute:

$ dana -sp ../server Distributor.o

Em um segundo terminal digite:

$ dana RemoteList.o

Em um terceiro terminal digite:

$ dana RemoteList.o 2011

A primeira composição do servidor que o Distribuidor monta é a versão local. Para distribuí-lo, digite distribute. Para tornar o servidor todo local novamente, digite local.
