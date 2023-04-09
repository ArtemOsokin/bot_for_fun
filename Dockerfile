# pull official base image
FROM python:alpine3.16

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

# copy project
COPY . /src/
EXPOSE 80

CMD ["python", "/src/run.py"]