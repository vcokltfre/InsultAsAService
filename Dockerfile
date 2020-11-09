FROM python:latest

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8193"]