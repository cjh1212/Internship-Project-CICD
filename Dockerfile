FROM python:3.8.2-alpine

RUN pip install pandas scikit-learn

COPY start.sh /start.sh
RUN chmod 777 /start.sh
COPY train.py /train.py
RUN chmod 777 /train.py
COPY final.csv /final.csv
RUN chmod 777 /final.csv

RUN pip install scikit-learn

RUN python3 /train.py
