FROM python:3.10

WORKDIR /app

COPY requirements.txt .
COPY setup.py .
COPY README.md .
COPY app.py .
# If you have other source code in src/, copy it as well:
COPY src/ ./src/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]
