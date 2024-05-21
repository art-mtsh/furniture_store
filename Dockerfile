# Use an official Python runtime as a base image
FROM python:alpine

# Install build dependencies
RUN apk add --no-cache gcc musl-dev postgresql-dev

# Install psycopg2
RUN pip install psycopg2

# Set the working directory in the container
WORKDIR app

# Copy the entire project directory into the container
COPY . app

# Copy SSL certificates into the container
COPY etc/fullchain.pem /etc/ssl/certs/fullchain.pem
COPY etc/privkey.pem /etc/ssl/private/privkey.pem

# Install dependencies
RUN pip install -r requirements.txt

# Copy SSL certificate
COPY dev_ssl.crt /usr/local/share/ca-certificates/dev_ssl.crt
RUN update-ca-certificates

# Expose port 8000
# EXPOSE 8000
# EXPOSE 443


# Run the Django development server
# CMD ["python", "backend/run_server.py"]


# Make sure the private key has the correct permissions
# RUN chmod 600 /etc/ssl/private/privkey.pem

# Expose port 443 for HTTPS
EXPOSE 443

# Run the command to start Gunicorn with HTTPS
CMD ["gunicorn", "--certfile=/etc/ssl/certs/fullchain.pem", "--keyfile=/etc/ssl/private/privkey.pem", "--bind", "0.0.0.0:443", "backend.wsgi:app"]