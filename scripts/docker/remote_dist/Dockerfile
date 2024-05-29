FROM ubuntu:24.04

RUN apt-get update && apt-get install -y wget unzip
RUN wget https://www.projectdana.com/download/ubu64/253 -O /dana.zip --no-check-certificate
RUN unzip /dana.zip -d /dana
RUN chmod +x /dana/dana /dana/dnc

COPY . ./home/remote-dist
ENV DANA_HOME=/dana/

ENV PATH="${PATH}:/dana/"
WORKDIR /home/remote-dist/distributor/

RUN ../compile-project.sh

ENTRYPOINT ["/bin/bash", "./../scripts/bash/remote_start.sh"]
