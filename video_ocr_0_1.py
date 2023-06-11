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
cap = cv2.VideoCapture()

def select_video():
    # Get the path to the selected video file.
    video_path = tk.filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])

    # If a video file has been selected, then open it with the video capture object.
    if video_path:
        cap.open(video_path)

        # Update the label to display the name of the selected video.
        video_name_label.config(text=video_path)


# Create a button to select a video from the local files.
select_video_button = tk.Button(window, text="Select Video", command=select_video)
select_video_button.pack()

# Create a label to display the name of the selected video.
video_name_label = tk.Label(window, text="No Video Selected")
video_name_label.pack()

# Create a label to display the text extracted from the video.
text_label = tk.Label(text_frame, text="")
text_label.pack()

# Start a loop to read frames from the video.
while True:
    # If a video has been selected, then read frames from the video.
    if cap.isOpened():
        ret, frame = cap.read()

        # Display the frame in the video frame.
        cv2.imshow('Video', frame)

        # Extract text from the frame.
        text = pytesseract.image_to_string(frame, lang='eng')

        # Display the text in the text frame.
        text_label.config(text=text)

    # Check if the user wants to quit.
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Close the video capture object.
cap.release()

# Close the window.
window.mainloop()

# This function is called when the "Select Video" button is clicked.
