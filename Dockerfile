FROM python:3.6-slim
MAINTAINER Mattherix

ENV PYTHONUNBUFFERED 1

RUN adduser --no-create-home django

RUN mkdir /social_road/
RUN chown django /social_road/
WORKDIR /social_road

COPY requirements.txt /social_road/
RUN pip install --no-cache -r requirements.txt

RUN apt-get update && apt-get install -y gdal-bin python3-gdal proj-bin

COPY ./staticfiles /social_road/staticfiles
COPY ./account /social_road/account
COPY ./algorithme_de_suggestion /social_road/algorithme_de_suggestion
COPY ./asserts /social_road/asserts
COPY ./core /social_road/core
COPY ./media /social_road/media
COPY ./post /social_road/post
COPY ./social_road /social_road/social_road
COPY manage.py /social_road
COPY ./voies_mel/voies_mel.shp /social_road/voies_mel.shp
