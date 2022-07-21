FROM ubuntu:latest
# USER root
RUN apt-get update && apt-get install -y python3.9 python3.9-dev
RUN pip install pandas scikit-learn
COPY start.sh /start.sh
COPY train.py /train.py

RUN pip install scikit-learn

CMD ["/start.sh"]
