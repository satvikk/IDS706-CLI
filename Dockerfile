FROM python:3.9-slim

WORKDIR /CLI

COPY ./requirements.txt /CLI
COPY ./setup.py /CLI
COPY ./checkifup.py /CLI

RUN	pip3 install -r requirements.txt
RUN pip3 install --editable .

ENTRYPOINT ["checkifup"]
