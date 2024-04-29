# Use an official Python runtime as a base image
FROM python:alpine

# Install build dependencies
RUN apk add --no-cache gcc musl-dev postgresql-dev

# Install psycopg2
RUN pip install psycopg2

# Copy the entire project directory into the container
COPY . app

# Set the working directory in the container
WORKDIR app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run the Django development server
# CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
CMD ["python", "backend/run_server.py"]
