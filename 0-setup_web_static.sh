#!/usr/bin/env bash
# Set up web server

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo "Hello world" | sudo tee /data/web_static/releases/test/index.html
CURRENT="/data/web_static/current"
if [ -L "$CURRENT" ]; then
    sudo rm "$CURRENT"
fi
sudo ln -s /data/web_static/releases/test/ "$CURRENT"
sudo chown -hR ubuntu:ubuntu /data
sudo sed -i "40i location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
