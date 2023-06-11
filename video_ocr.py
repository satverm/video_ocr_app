# video and text from video source like youtube
# and convert it for live use rather than only using for viewing


import cv2
import pytesseract
import tkinter as tk

# Create a Tkinter window.
window = tk.Tk()

# Create two frames.
video_frame = tk.Frame(window)
text_frame = tk.Frame(window)

# Add the frames to the window.
video_frame.pack()
text_frame.pack()

# Create a video capture object.
cap = cv2.VideoCapture(0)

# Start a loop to read frames from the video.
while True:
    # Read a frame from the video.
    ret, frame = cap.read()

    # Display the frame in the video frame.
    cv2.imshow('Video', frame)

    # Extract text from the frame.
    text = pytesseract.image_to_string(frame, lang='eng')

    # Display the text in the text frame.
    text_label = tk.Label(text_frame, text=text)
    text_label.pack()

    # Check if the user wants to quit.
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Close the video capture object.
cap.release()

# Close the window.
window.mainloop()
