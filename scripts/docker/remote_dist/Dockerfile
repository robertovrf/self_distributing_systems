FROM dana:253

COPY . ./home/remote-dist
WORKDIR /home/remote-dist/
RUN ./build.sh

WORKDIR /home/remote-dist/distributor/
ENTRYPOINT ["dana", "-sp", "../constant", "RemoteDist.o"]
