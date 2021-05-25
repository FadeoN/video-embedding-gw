FROM python:3.7-slim

COPY requirements.txt /

RUN python3 -m pip install -r requirements.txt

COPY . /video-embedding-gw

WORKDIR /video-embedding-gw

ADD . /video-embedding-gw

EXPOSE 5005

CMD ["python3", "main.py"]