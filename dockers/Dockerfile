FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your test code or app
COPY . .

# Entry point or default command
CMD ["pytest"]
