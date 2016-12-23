# 331.3 KB context, #72.11MB base, 352.3 MB final
FROM python:2-alpine
MAINTAINER Cameron Whiting "thetoxicarcade@gmail.com"
RUN apk add -q --update gcc g++ make libffi-dev openssl-dev
#115.9 MB
#for l in $(cat t); do apk add $l 1>/dev/null || echo $l; done
#build-base util-linux #linux-headers musl-dev #py-pip py-twisted python-dev
ADD requirements.txt /
# 269 B
RUN pip install -q -r requirements.txt nose2 setuptools-lint pylint
# 123.8 MB
ADD . /code
# 174.1 kB
WORKDIR /code
RUN python setup.py build install 1>/dev/null
# 46.37 kB
RUN python setup.py bdist_wheel 1>/dev/null
# 9.02 kB
RUN python setup.py test 1>/dev/null
# 156 kB
RUN python setup.py lint || echo "Code Quality failing..."
# 183.1 kB
EXPOSE 8800
# most of that size is in adding development headers & compilers
# for installing things like py-cryptography. Chaining them and
# then removing (via apk) the compilers & such may save space?