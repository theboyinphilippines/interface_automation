FROM python:3.8-alpine
MAINTAINER Tester
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD python -m pytest --alluredir report --clean-alluredir
