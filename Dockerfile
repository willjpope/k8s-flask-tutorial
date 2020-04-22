FROM python:3.6-jessie

RUN apt-get update \
 && apt-get install --yes --no-install-recommends \
        apt-transport-https \
        curl \
        gnupg \
        unixodbc-dev \

RUN yum install -y unixODBC
RUN yum install -y unixODBC-devel

RUN mkdir -p /opt/unixodbc \
  && chown 1000:0 /opt/unixodbc

USER 1000

WORKDIR /opt/unixodbc

ARG NAME=unixODBC
ARG VERSION=2.3.6

RUN curl http://www.unixodbc.org/${NAME}-${VERSION}.tar.gz | tar -xzC /opt/unixodbc \
  && cd $NAME-$VERSION \
  && ./configure --prefix=/usr \
  && make \
  && mkdir /tmp/installdir \
  && make install DESTDIR=/tmp/installdir \
  && fpm -s dir -t deb -n $NAME -v $VERSION \
  -C /tmp/installdir \
  -p ${NAME}_VERSION_ARCH.deb \
  usr

WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app

ENV PORT 8080
CMD ["gunicorn", "app:app", "--config=config.py"]
