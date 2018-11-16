FROM alpine:latest

RUN apk add --update py2-pip
RUN pip install --upgrade pip
RUN pip install flask flask-jsonpify flask-sqlalchemy flask-restful
RUN mkdir simpleRESTAPI

COPY heroes.db /simpleRESTAPI/
COPY simpleRESTAPI.py /simpleRESTAPI/

EXPOSE 5002

WORKDIR simpleRESTAPI/
CMD ["python", "simpleRESTAPI.py"]