#!/bin/bash
# Simple sandbox setup script

# Create a new user
sudo useradd -m sandboxuser

# Restrict the user
sudo usermod -L sandboxuser

# Setup chroot environment
sudo mkdir -p /home/sandboxuser/chroot
sudo debootstrap --variant=minbase buster /home/sandboxuser/chroot http://deb.debian.org/debian/

echo "Sandbox environment setup complete."
