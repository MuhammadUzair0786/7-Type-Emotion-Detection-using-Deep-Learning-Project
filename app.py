from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os
import warnings

# Initialize Flask app
app = Flask(__name__)

# Ignore TensorFlow warnings
warnings.filterwarnings('ignore', category=UserWarning, module='tensorflow')

# Load pre-trained model
model = load_model('Uzair-Emotion_model.h5', compile=False)

# Emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    filepath = None

    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join('static', 'uploaded_image.jpg')
            file.save(filepath)

            # Preprocess image
            img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (48, 48))
            img = img.astype('float32') / 255.0
            img = np.expand_dims(img, axis=(0, -1))

            # Predict emotion
            pred = model.predict(img)
            predicted_emotion = emotion_labels[np.argmax(pred)]

            # Render prediction
            return render_template('index.html', prediction=predicted_emotion, image_file=filepath)

    return render_template('index.html', prediction=prediction, image_file=filepath)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
