FROM ramadhani892/ramubot:master

# Rama ganteng, Yang hapus credit, Lo babi heheh
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================
    && chmod 777 /home/ram-ubot \
    && mkdir /home/ram-ubot/bin/
WORKDIR /home/ram-ubot/


CMD ["python3", "-m", "userbot"]
