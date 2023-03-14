# Video Stream Bitrate and Frame Rate
This repository contains two Python scripts that can get the bitrate and frame rate of a video stream using FFprobe.

# Requirements
 * Python 3
 * FFprobe (https://ffmpeg.org/ffprobe.html)
# Usage
* To run the first script, use the command python OpenCV-analyze.py
* To run the second script, use the command python ffprobe-analyze.py
* Enter the stream URL when prompted
* The scripts will print the bitrate and frame rate of the stream, or an error message if the command failed
# Example
```bash
$ python ffprobe-analyze.py
Enter the stream URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Bitrate: 128000
Frame rate: 25/1
```

# M3U8 Stream Download Duration Script

This script downloads all the TS files in an M3U8 stream and calculates the duration of the last download.
# Requirements

  -   Bash
  -  cURL

# Usage

   1-  Save the script to a file, for example download_duration.sh.
   2-  Replace https://example.com/stream.m3u8 with the actual URL of the M3U8 stream, and /path/to/output/directory with the path to the directory where you want the TS files to be downloaded.
   3- Open a terminal and navigate to the directory where the script is saved.
   4- Make the script executable by running chmod +x download_duration.sh.
   5- Run the script by typing ./download_duration.sh in your terminal.
   6- The script will download all the TS files in the M3U8 stream to the specified directory, and output the duration of the last download in seconds and milliseconds.

# License

This script is released under the MIT License. Feel free to use, modify, and distribute it as you wish.
