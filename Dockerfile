############################
# Final container
############################
FROM registry.cto.ai/official_images/python:latest

RUN pip3 install cto-ai

WORKDIR /ops

ADD . .

COPY requirements.txt .

RUN pip3 install --no-cache-dir --no-warn-script-location -r requirements.txt
