FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /
COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . ./
# training the model
WORKDIR /./chatbot_model/
RUN python3 training.py

WORKDIR /
EXPOSE 8000