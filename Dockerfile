FROM ubuntu:latest
USER root
RUN apt-get update -y
RUN apt-get install -y python
RUN pip install pandas scikit-learn
COPY start.sh /start.sh
COPY train.py /train.py

RUN pip install scikit-learn

CMD ["/start.sh"]
