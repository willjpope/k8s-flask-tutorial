FROM python:3.6-jessie

RUN yum groupinstall "Development Tools" -y
RUN yum -y install wget zlib-devel bzip2-devel openssl-devel ncurses-devel 
sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz- 
devel  unixODBC-devel
RUN wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz
RUN tar xJf Python-3.6.4.tar.xz
RUN cd Python-3.6.4 && ./configure --enable-optimizations --enable-loadable- 
sqlite-extensions --prefix=/usr --enable-shared --enable-loadable-sqlite- 
extensions --with-system-expat --with-system-ffi --with-ensurepip=yes && 
make && make install
RUN chmod -v 755 /usr/lib/libpython3.6m.so
RUN chmod -v 755 /usr/lib/libpython3.so
RUN echo '/usr/local/lib' >> /etc/ld.so.conf
RUN ldconfig -v
RUN curl -k  https://packages.microsoft.com/config/rhel/7/prod.repo > 
/etc/yum.repos.d/mssql-release.repo
RUN yum remove unixODBC-utf16 unixODBC-utf16-devel
RUN ACCEPT_EULA=Y yum -y install msodbcsql17
RUN ACCEPT_EULA=Y yum -y install mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN source ~/.bashrc

WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app

ENV PORT 8080
CMD ["gunicorn", "app:app", "--config=config.py"]
