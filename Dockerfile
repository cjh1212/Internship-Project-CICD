FROM python:latest

USER root

RUN pip install scikit-learn

CMD ["python3", "print.py"]
