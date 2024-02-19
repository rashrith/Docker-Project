# Use the official Python image from Docker Hub
FROM python:3.8-alpine

WORKDIR /home
COPY main.py .

# Create the /home/output directory inside the container
RUN mkdir -p /home/output

WORKDIR  /home/data
COPY . .

# Run the command when the container starts
CMD ["python", "/home/main.py"]
