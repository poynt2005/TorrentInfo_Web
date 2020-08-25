FROM node:current-alpine AS base

WORKDIR /root

COPY . /root

RUN npm i && npm run build

FROM debian:buster-slim

RUN apt-get update
RUN apt-get install -y python-libtorrent python-pip
RUN mkdir /root/torrentfiles && mkdir /root/dist && echo "[]" > /root/torrentfiles/history.json
RUN pip install flask gunicorn

WORKDIR /root

COPY --from=base /root/app.py /root/torrentinfo.py /root/readJson.py /root/
COPY --from=base /root/dist /root/dist

EXPOSE 8080
EXPOSE 6881

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]