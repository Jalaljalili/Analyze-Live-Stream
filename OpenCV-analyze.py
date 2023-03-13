import cv2
import time

# Get the stream URL from the user
stream_url = input("Enter the stream URL: ")

# Create a VideoCapture object
cap = cv2.VideoCapture(stream_url)

# Check if the stream is opened successfully
if not cap.isOpened():
    print("Error opening stream")

# Get the stream properties
fps = cap.get(cv2.CAP_PROP_FPS) # frames per second
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # width in pixels
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # height in pixels
bitrate = cap.get(cv2.CAP_PROP_BITRATE) # bitrate in bits per second
scale = cap.get(cv2.CAP_PROP_POS_AVI_RATIO) # relative position of the video file
speed = cap.get(cv2.CAP_PROP_SPEED) # speed of the video relative to the source

# Print the stream properties
print(f"FPS: {fps}")
print(f"Resolution: {width} x {height}")
print(f"Bitrate: {bitrate}")
print(f"Scale: {scale}")
print(f"Speed: {speed}")

# Start a timer
start = time.time()

# Initialize a frame counter
frame_count = 0

# Loop until the stream is over
while cap.isOpened():
    # Read a frame from the stream
    ret, frame = cap.read()

    # Check if the frame is valid
    if not ret:
        break

    # Increment the frame counter
    frame_count += 1

    # Display the frame
    cv2.imshow("Frame", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Stop the timer
end = time.time()

# Release the VideoCapture object
cap.release()

# Destroy all windows
cv2.destroyAllWindows()

# Calculate the actual fps
actual_fps = frame_count / (end - start)

# Print the actual fps
print(f"Actual FPS: {actual_fps}")
