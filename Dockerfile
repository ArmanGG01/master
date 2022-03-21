FROM ramadhani892/ramubot:master

# Rama ganteng, Yang hapus credit, Lo babi heheh
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================
##

RUN git clone -b RAM-UBOT https://github.com/ramadhani892/RAM-UBOT /home/Developer/
WORKDIR /home/Developer/


CMD ["python3", "-m", "userbot"]
