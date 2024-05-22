# # Use an official Python runtime as a base image
# FROM python:alpine
#
# # Install build dependencies
# RUN apk add --no-cache gcc musl-dev postgresql-dev
#
# # Install psycopg2
# RUN pip install psycopg2
#
# # Copy the entire project directory into the container
# COPY . /app
#
# # Set the working directory in the container
# WORKDIR /app
#
# # Install dependencies
# RUN pip install -r requirements.txt
#
# # Expose port 80
# EXPOSE 80
#
# # Run the Django development server
# CMD ["python", "backend/run_server.py"]

# Stage 1: Build Django app
FROM python:3.10-alpine as builder

# Install build dependencies
RUN apk add --no-cache gcc musl-dev postgresql-dev

# Install psycopg2
RUN pip install psycopg2

# Set working directory
WORKDIR /app

# Copy the entire project directory into the container
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Stage 2: Build Nginx with Django app
FROM nginx:alpine

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Copy SSL certificates
COPY certs /etc/nginx/certs

# Copy Django app from builder stage
COPY --from=builder /app /app

# Set working directory
WORKDIR /app

# Expose ports
EXPOSE 80 443

# Run the Django development server
CMD ["sh", "-c", "python backend/run_server.py & nginx -g 'daemon off;'"]
