FROM ramadhani892/ramagans:slim-buster

# Rama ganteng, Yang hapus credit, Lo babi heheh
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================
##

RUN git clone -b RAM-UBOT https://github.com/ramadhani892/RAM-UBOT /home/Developer/ \
    && chmod 777 /home/Developer \
    && mkdir /home/Developer/bin/
WORKDIR /home/Developer/


CMD ["python3", "-m", "userbot"]
