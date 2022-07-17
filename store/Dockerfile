FROM apache/skywalking-python:0.7.0-grpc-py3.6

# FROM python:3.6.3

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY store.py .
EXPOSE 5000
CMD python store.py