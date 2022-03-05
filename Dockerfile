FROM skyzuxzy/skyzu-userbot:buster


RUN git clone -b RAM-UBOT https://github.com/ramadhani892/RAM-UBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools

WORKDIR /root/userbot

CMD ["python3", "-m", "userbot"]
