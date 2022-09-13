FROM hitokizzy/ibel:slim-buster

RUN git clone -b master https://github.com/ramadhani892/RAM-UBOT/ \
    && chmod 777 /home/master \
    && mkdir /home/master/bin/

WORKDIR /home/master/

CMD ["python3", "-m", "rams"]
