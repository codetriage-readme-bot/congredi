FROM python:2-alpine
MAINTAINER Cameron Whiting "thetoxicarcade@gmail.com"
RUN apk add --update gcc g++ make libffi-dev openssl-dev
ADD requirements.txt /
RUN pip install -r requirements.txt && \
	pip install nose2 setuptools-lint
ADD . /code
WORKDIR /code
RUN python setup.py build && \
	python setup.py test && \
	python setup.py install && \
	python setup.py lint || echo "Lint failing..."
EXPOSE 5000
