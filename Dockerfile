FROM python:3.8.5-slim-buster

# Set working directory inside the container
WORKDIR /app

# Copy necessary files
COPY requirements.txt .
COPY setup.py .
COPY README.md .
COPY app.py .
COPY src/ ./src/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port your app runs on
EXPOSE 8080

# Run your main application
CMD ["python3", "app.py"]
