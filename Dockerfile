FROM python:3.8
MAINTAINER Tester
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
#ENTRYPOINT ["./python -m pytest --alluredir report --clean-alluredir"]
ENTRYPOINT ["./pytest --alluredir report --clean-alluredir"]
