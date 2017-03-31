FROM alpine:latest
RUN apk add --update python py2-pip && adduser -D local
RUN mkdir local && pip install --upgrade pip && pip install awscli jinja2 shell
COPY *.py /home/local/
COPY bootstrap /home/local/bootstrap
RUN cd /home/local && mkdir scripts && python setup.py install 
USER local
WORKDIR /home/local
CMD python run.py