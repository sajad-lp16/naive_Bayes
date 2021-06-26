FROM python:latest
WORKDIR /mehdi
COPY requirements.txt .
COPY Multi_practice.py .
RUN pip install -r requirements.txt
CMD python ./Multi_practice.py
