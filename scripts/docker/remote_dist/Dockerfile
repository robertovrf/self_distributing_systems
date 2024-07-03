FROM dana:253

COPY . ./home/remote-dist
WORKDIR /home/remote-dist/distributor/

RUN ../compile-project.sh

ENTRYPOINT ["/bin/bash", "./../scripts/bash/remote_start.sh"]
