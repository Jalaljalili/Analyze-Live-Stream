import subprocess
import json

# Get the stream URL from the user
stream_url = input("Enter the stream URL: ")

# Execute FFprobe as a sub-process and get a CompletedProcess object
command = ["ffprobe", "-print_format", "json", "-show_entries", "stream=bit_rate,r_frame_rate", stream_url]
process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Check the return code of the sub-process
if process.returncode == 0:
    # Convert the returned string to a dictionary
    data = json.loads(process.stdout)

    # Get the bitrate and frame rate from the dictionary
    bitrate = data["streams"][0]["bit_rate"]
    frame_rate = data["streams"][0]["r_frame_rate"]

    # Print the bitrate and frame rate
    print(f"Bitrate: {bitrate}")
    print(f"Frame rate: {frame_rate}")
else:
    # Print the error message
    print(f"Error: {process.stderr}")