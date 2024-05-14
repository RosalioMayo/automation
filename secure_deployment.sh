#!/bin/bash
# Script for secure deployment on AWS

# Update and install required packages
sudo apt-get update
sudo apt-get install -y fail2ban ufw

# Enable UFW
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow http
sudo ufw enable

echo "Basic security configurations applied."
