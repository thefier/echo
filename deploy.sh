#!/bin/bash
set -e

# Update and install dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install -y docker.io docker-compose git ufw

# Enable docker service and add current user
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Build and start containers
docker-compose up -d --build

# Setup UFW firewall
sudo ufw allow OpenSSH
sudo ufw allow 5000/tcp
sudo ufw --force enable

echo "✅ Deploy complete! Your API is running on port 5000."
