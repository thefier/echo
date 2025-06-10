FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Clone EchoNet-Dynamic repo
RUN git clone https://github.com/echonet/dynamic.git echonet_model

# Copy application code
COPY app.py .
COPY utils.py .
COPY templates ./templates

CMD ["python", "app.py"]
