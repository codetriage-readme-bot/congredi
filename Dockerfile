FROM python:2-alpine
# 72.11MB - base
MAINTAINER Cameron Whiting "thetoxicarcade@gmail.com"
ADD requirements.txt /
# 269 B
RUN apk add --update gcc g++ make libffi-dev openssl-dev && \
	pip install -r requirements.txt setuptools-green green setuptools-lint pylint && \
	apk del gcc g++ make && \
	apk add libstdc++ libcrypto1.0 openssl-dev
#131.4 MB - FIXME on the del-then-re-add-libstdc++

# -- The above is a "base" layer. Don't touch it for faster builds. --

ADD . /code
# 184.8 kB / 331.3 KB context (.dockerignore)
WORKDIR /code
RUN python setup.py green && \
    python setup.py build bdist_wheel install 1>/dev/null && \
	find . -type f -name "*.pyc" -delete
# 186.7 kB - Could be removing more files.
EXPOSE 8800

# Originally was 352.3 MB, now around 205.9 MB.
# 141.4 MB of that is libs...
