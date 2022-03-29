# syntax=docker/dockerfile:1
FROM python:3.9.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

EXPOSE 42042

CMD [ "python" , "manage.py", "runserver", "42042" ]
