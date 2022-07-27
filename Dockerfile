FROM python:latest

RUN pip install pandas datasets transformers Flask gunicorn

COPY ./app.py /app
COPY ./templates /app/templates

WORKDIR /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
