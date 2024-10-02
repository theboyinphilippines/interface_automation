FROM python:3.8
MAINTAINER Tester
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD ["python -m pytest --alluredir report --clean-alluredir"]

