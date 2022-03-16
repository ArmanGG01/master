FROM ramadhani892/ram-ubot:slim-buster
# Rama ganteng, Yang hapus credit, Lo babi heheh
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================
##

RUN git clone -b RAM-UBOT https://github.com/ramadhani892/RAM-UBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools

WORKDIR /root/userbot

CMD ["python3","-m","userbot"]
