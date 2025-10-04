FROM python:3.8.5-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt


# Run your main application
CMD ["python3", "app.py"]
