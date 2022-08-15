FROM hitokizzy/ibel:slim-buster

RUN git clone -b master https://github.com/ramadhani892/RAM-UBOT /home/rams/

WORKDIR /home/rams

CMD ["python3","-m","rams"]
