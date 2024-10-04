FROM python:3.8-alpine
MAINTAINER Tester
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD python -m pytest --alluredir report --clean-alluredir
