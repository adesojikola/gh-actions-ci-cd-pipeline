# Use the official Python image with Alpine as a base
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the local files into the container at /app
COPY . /app/

# Specify the command to run on container start
CMD ["python", "src/main.py"]
