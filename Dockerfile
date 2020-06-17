FROM anthonyguerreiro/libtorrent-python

RUN apk add --update py-pip \
 && pip install flask gunicorn
 
WORKDIR /app

COPY . /app

EXPOSE 8080

EXPOSE 6881

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]