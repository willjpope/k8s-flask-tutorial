FROM python:3.6-jessie

RUN apt update

WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

RUN yum install -y unixODBC
RUN yum install -y unixODBC-devel

ADD . /app

ENV PORT 8080
CMD ["gunicorn", "app:app", "--config=config.py"]
