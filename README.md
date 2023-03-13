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
