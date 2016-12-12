FROM python:2-alpine
MAINTAINER Cameron Whiting "thetoxicarcade@gmail.com"
RUN apk add --update gcc g++ make libffi-dev openssl-dev
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD . /code
WORKDIR /code
RUN python setup.py build && \
	python setup.py install
RUN python setup.py test && \
	python setup.py lint || echo "Code Quality failing..."
EXPOSE 8800