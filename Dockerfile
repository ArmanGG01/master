FROM ramadhani892/ram-ubot:slim-buster
# Rama ganteng, Yang hapus credit, Lo babi heheh
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================
##

RUN git clone -b RAM-UBOT https://github.com/ramadhani892/RAM-UBOT /home/ram-ubot/ \
    && chmod 777 /home/ram-ubot \
    && mkdir /home/ram-ubot/bin/

WORKDIR /home/ram-ubot/

CMD ["python3", "-m", "userbot"]
