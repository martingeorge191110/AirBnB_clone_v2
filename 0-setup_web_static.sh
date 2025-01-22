#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Alx
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sh -c 'echo "server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;
        location /redirect_me {
                 return 301 http://google.com;
        }

        error_page 404 /404.html;

        location = /404.html {
                root /usr/share/nginx/html;
                internal;
        }

        location / {
                try_files $uri $uri/ =404;
        }

        location /hbnb_static {
                alias /data/web_static/current/;
        }
}" > /etc/nginx/sites-available/default'
sudo service nginx restart
