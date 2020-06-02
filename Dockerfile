FROM python:3.6-slim
MAINTAINER Mattherix

ENV PYTHONUNBUFFERED 1

RUN adduser --no-create-home socialroad

RUN mkdir /social_road/
RUN chown socialroad /social_road/
WORKDIR /social_road

COPY Makefile /social_road/
COPY Makefile.test /social_road/
RUN apt-get update
RUN apt-get install -y make

COPY requirements.txt /social_road/
RUN make install

COPY ./staticfiles /social_road/staticfiles
COPY ./account /social_road/account
COPY ./algorithme_de_suggestion /social_road/algorithme_de_suggestion
COPY ./asserts /social_road/asserts
COPY ./core /social_road/core
COPY ./media /social_road/media
COPY ./post /social_road/post
COPY ./social_road /social_road/social_road
COPY manage.py /social_road

USER socialroad
