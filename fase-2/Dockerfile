# Use the official Python image as the base image
FROM python:3.10.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any required dependencies
RUN pip install -r requirements.txt

# Expose port in case of need
EXPOSE 8080

# Specify the command to run your application
CMD ["python", "/app/scripts/train.py"]