FROM ubuntu:latest
USER root
RUN apt-get update -y
RUN apt-get install -y python3-pip

RUN pip install pandas scikit-learn

COPY start.sh /start.sh
RUN chmod 777 /start.sh
COPY train.py /train.py
RUN chmod 777 /train.py
COPY final.csv /final.csv
RUN chmod 777 /final.csv

RUN pip install scikit-learn

CMD ["bin/bash", "/start.sh"]
