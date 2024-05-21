#!/bin/sh

# Start Nginx in the background
nginx &

# Ensure the directory for challenge files exists
mkdir -p /var/www/certbot

# Obtain SSL certificates using Certbot
certbot certonly --webroot -w /var/www/certbot -d furnishop-back.pp.ua --non-interactive --agree-tos --email art.mtsh@gmail.com

# Reload Nginx to apply the certificates
nginx -s reload

# Start a cron job to renew certificates periodically
echo "0 0,12 * * * root certbot renew --post-hook 'nginx -s reload'" > /etc/crontabs/root
crond -f &
