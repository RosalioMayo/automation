#!/bin/bash
# Simple memory capture script

output_file="memory_dump.raw"
sudo dd if=/dev/mem of=$output_file bs=1M
echo "Memory dump saved to $output_file."
