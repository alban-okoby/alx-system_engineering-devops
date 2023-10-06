#!/usr/bin/env bash
## Description
#!/bin/bash

# Function to extract sender, receiver, and flags from a message
extract_info() {
    sender=$(echo "$1" | grep -oP 'Sender: \K(.+?)(?=,)')
    receiver=$(echo "$1" | grep -oP 'Receiver: \K(.+?)(?=,)')
    flags=$(echo "$1" | grep -oP 'Flags: \K(.+?)$')

    echo "$sender,$receiver,$flags"
}

# Sample text message data (replace with your actual data file)
data_file="text_messages.txt"

# Check if the data file exists
if [ ! -f "$data_file" ]; then
    echo "Data file not found: $data_file"
    exit 1
fi

# Process each line in the data file
while read -r line; do
    info=$(extract_info "$line")
    if [ -n "$info" ]; then
        echo "$info"
    fi
done < "$data_file"
