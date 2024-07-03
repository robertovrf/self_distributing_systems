FROM ubuntu:24.04

RUN apt-get update && apt-get install -y wget unzip
RUN wget https://www.projectdana.com/download/ubu64/253 -O /dana.zip --no-check-certificate
RUN unzip /dana.zip -d /dana
RUN rm /dana.zip
RUN chmod +x /dana/dana /dana/dnc

ENV DANA_HOME=/dana/
ENV PATH="${PATH}:/dana/"
