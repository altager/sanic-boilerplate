FROM python:3.6

ENV app /opt/app

RUN mkdir -p ${app}
WORKDIR ${app}

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . ${app}
