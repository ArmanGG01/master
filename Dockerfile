FROM ramadhani892/ramubot:dragons

RUN git clone -b master https://github.com/ramadhani892/ram-ubot home/master/ \
    && chmod 777 /home/master \
    && mkdir /home/master/bin/

WORKDIR /home/master/

CMD ["python3", -m", "rams"]
