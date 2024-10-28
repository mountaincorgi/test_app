FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src
RUN pip install --upgrade pip
COPY requirements.txt /src/
RUN pip install -r requirements.txt
COPY . /src/
WORKDIR /src/testapp

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
