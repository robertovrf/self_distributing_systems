# Projeto Final de Graduação

## Para compilar o projeto:

Dê permissão para o arquivo "build.sh" executar:
```sh
$ chmod +x build.sh
```

Execute-o:
```sh
$ ./build.sh
```

## Para executar o servidor:

Entre na pasta __server__ em um terminal e digite:
```sh
$ dana main.o
```

Note: Não há a necessidade de executar o servidor desta forma se for executar o Distributor, seguindo as instruções abaixo.

## Para executar o idistribuidoelocal e remote):

Abra três terminais na pasta _distributor_. No primeiro execute:
```sh
$ dana -sp "../server;../readn" Distributor.o
```

Em um segundo terminal digite:
```sh
$ dana -sp ../readn RemoteDist.o
```

Em um terceiro terminal digite:
```sh
$ dana -sp ../readn RemoteDist.o 8082 2011
```

A primeira composição do servidor que o Distribuidor monta é a versão local. Para distribuí-lo, digite help e escolhar qual opção de distribuir. Para tornar o servidor toidor todo local novamente, digite local.

## Para executar o script em Python:

Entre na pasta "python_scripts" e depois execute:
```sh
$ python3 example.py
```

## Para simular o ambiente Kubernetes localmente:

Usamos [kind](https://kind.sigs.k8s.io/) para simular um ambiente Kubernetes localmente e [cloud-provider-kind](https://github.com/kubernetes-sigs/cloud-provider-kind) para fornecer o endereço IP para os Load Balancers locais.

Para criar o ambiente, você deve ter um ambiente com [docker](https://www.docker.com/), [podman](https://podman.io/) ou [nerdctl](https://github.com/containerd/nerdctl) instalado. Depois disso, sugerimos instalar o [go](https://go.dev) 1.22+ através do [goenv](https://github.com/go-nv/goenv) e executar os seguintes comandos:
```sh
$ go install sigs.k8s.io/kind@v0.23.0
$ go install sigs.k8s.io/cloud-provider-kind@latest
$ sudo install $(go env GOPATH)/bin/cloud-provider-kind /usr/local/bin
$ kind create cluster
```

Em um terminal separado, você precisa manter o Cloud Provider em execução para fornecer o IP local:
```sh
$ sudo cloud-provider-kind
```

Agora, precisamos configurar a imagem base do Dana:
```sh
$ ./scripts/bash/build-dana.sh
```

Ao executar localmente, você também pode querer criar uma imagem `remote-dist` local. Nesse caso, você pode construir e carregar a imagem Docker executando o seguinte script:
```sh
$ ./scripts/bash/build-remote-dist.sh
```

## Para executar o Implementation Provider (Dynamic Sharding):
Com um ambiente Kubernetes configurado, você pode executar o Implementation Provider com o seguinte comando:
```sh
$ ./build-and-run-implementation-provider.sh
```

Após a execução, você deve configurar o IP associado ao servidor na variável `IMPLEMENTATION_PROVIDER_HOST` no arquivo `ListCPDynamicShardin.dn` e executar novamente o Distributor. Isso é suficiente para poder selecionar a implementação "dynamic".