FROM python:latest

RUN pip install pandas datasets transformers Flask gunicorn

RUN mkdir -p /app/templates
RUN mkdir -p /app/model

COPY ./app.py /app
COPY ./templates/index.html /app/templates
COPY ./templates/result.html /app/templates
COPY ./model/config.json /app/model
COPY ./model/pytorch_model.bin /app/model
COPY ./model/training_args.bin /app/model

WORKDIR /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
