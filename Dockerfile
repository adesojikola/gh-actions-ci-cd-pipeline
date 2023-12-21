# Use the official Python image with Alpine as a base
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app/

# Copy the local files into the container at /app/
COPY . /app/

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the port that your Flask app will run on
EXPOSE 5000

# Specify the command to run on container start
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0"]
