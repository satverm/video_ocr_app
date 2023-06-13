# crrate a machine learning model to extract text from images

import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, LSTM

# Load the image
image = cv2.imread("img1.png")

# Convert the image to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize the image to 28x28 pixels
resized_image = cv2.resize(grayscale_image, (28, 28))

# Normalize the image
normalized_image = resized_image / 255.0

# Create the model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Train the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(normalized_image, np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), epochs=10)

# Recognize the text in the image
prediction = model.predict(normalized_image)
index = np.argmax(prediction)
text = str(index)

# Print the text
print(text)
