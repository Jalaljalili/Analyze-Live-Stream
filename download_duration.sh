#!/bin/bash

# Define the URL of the M3U8 stream and the output directory for the downloaded files
M3U8_URL="https://example.com/stream.m3u8"
OUTPUT_DIR="/path/to/output/directory"

# Download the M3U8 file and extract the URLs of the TS files
TS_URLS=($(curl -s "$M3U8_URL" | grep -v "#" | awk '{print $0}' | sed "s|^/|$M3U8_URL/|"))

# Loop through the TS URLs and download each file
START_TIME=$(date +%s.%N)
for URL in "${TS_URLS[@]}"; do
    FILENAME=$(basename "$URL")
    curl -s -o "$OUTPUT_DIR/$FILENAME" "$URL"
    END_TIME=$(date +%s.%N)
done

# Calculate the duration of the last download
DURATION=$(echo "$END_TIME - $START_TIME" | bc)

# Print the duration in seconds and milliseconds
printf "Last TS download duration: %.3f seconds\n" "$DURATION"
