#!/bin/bash
# Simple security audit script

echo "Running security audit..."

# Check for password expiration policy
if grep -q "PASS_MAX_DAYS" /etc/login.defs; then
    echo "Password expiration policy is set."
else
    echo "Password expiration policy is not set."
fi

# Check for SSH root login
if grep -q "PermitRootLogin no" /etc/ssh/sshd_config; then
    echo "SSH root login is disabled."
else
    echo "SSH root login is enabled."
fi
