FROM python:latest

RUN pip install pandas datasets transformers Flask gunicorn

RUN mkdir /app/templates

COPY ./app.py /app
COPY ./templates /app/templates
COPY ./model /app

WORKDIR /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
