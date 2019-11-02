FROM python:3.6.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /api
WORKDIR /api
COPY requirements.txt /api/
RUN pip install -r requirements.txt
COPY . /api/
