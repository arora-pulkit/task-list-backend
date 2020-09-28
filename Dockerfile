#Using the lightweight alpine image to get python 3.8
FROM python:3.8-alpine

RUN apk update

#Define working directory
WORKDIR /usr/app

#Setting up virtual env
RUN python -m venv venv

#Adding source code
COPY bootstrap.sh requirements.txt ./
COPY src ./src
COPY data ./data

#Installing packages
RUN pip install -r requirements.txt

#Starting app on port 5000
EXPOSE 5000
ENTRYPOINT ["/usr/app/bootstrap.sh"]