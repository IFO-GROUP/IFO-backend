FROM python:3.9.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

RUN python manage.py collectstatic

EXPOSE 42042

CMD [ "python" , "manage.py", "runserver", "0.0.0.0:42042" ]
