# Use the official Python base image
FROM python:3.13

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY app.py .

# Run the Python script
CMD ["python", "app.py"]


#Build the Docker image
docker build -t hello-docker .
#Run the Docker container
docker run hello-docker


