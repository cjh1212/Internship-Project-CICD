FROM python:latest

RUN pip install pandas datasets transformers Flask gunicorn
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

RUN mkdir -p /app/templates
RUN mkdir -p /app/model
RUN mkdir -p /app/tokenization

COPY ./app.py /app
COPY ./templates/index.html /app/templates
COPY ./templates/result.html /app/templates
COPY ./model/config.json /app/model
COPY ./model/pytorch_model.bin /app/model
COPY ./model/training_args.bin /app/model
COPY ./tokenization/config.json /app/tokenization
COPY ./tokenization/special_tokens_map.json /app/tokenization
COPY ./tokenization/tokenizer.json /app/tokenization
COPY ./tokenization/tokenizer_config.json /app/tokenization
COPY ./tokenization/vocab.txt /app/tokenization

WORKDIR /app

CMD ["python3", "app.py"]
