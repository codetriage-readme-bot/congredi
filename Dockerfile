FROM python:2-alpine
MAINTAINER Cameron Whiting "thetoxicarcade@gmail.com"
RUN apk add --update gcc g++ make libffi-dev openssl-dev
ADD requirements.txt /
RUN pip install -r requirements.txt nose2 setuptools-lint pylint
ADD . /code
WORKDIR /code
RUN python setup.py build install
RUN python setup.py test
RUN python setup.py lint || echo "Code Quality failing..."
EXPOSE 8800