FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
COPY setup.py ./
COPY README.md ./
COPY src/ ./src/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "src/car_sale_price_prediction/app.py"]
