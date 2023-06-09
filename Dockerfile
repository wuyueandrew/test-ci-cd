FROM bitnami/python:3.9.15

RUN mkdir /opt/test-ci-cd

COPY . /opt/test-ci-cd

RUN /opt/bitnami/python/bin/python3.9 -m pip install -r /opt/test-ci-cd/requirements.txt
