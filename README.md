# 7-Type Emotion Detection using Deep Learning

## 🧠 Overview

This project presents a custom Convolutional Neural Network (CNN) for detecting and classifying human facial expressions into seven emotions: **Angry, Disgust, Fear, Happy, Sad, Surprise, and Neutral**. The model is trained on grayscale facial images and achieves approximately **70% validation accuracy** and **67% training accuracy**. The final model is deployed as a Flask web application, enabling users to upload images and receive real-time emotion predictions.

---

## 📂 Project Structure
Type_Emotion_Detection.ipynb # Jupyter Notebook for model training & evaluation app.py # Flask web application backend Uzair-Emotion_model.h5 # Trained CNN model weights static/ uploaded_image.jpg # Uploaded image for prediction templates/ index.html # Frontend HTML template .idea/ # IDE configuration files README.md # Project

---

## 📈 Model Highlights

- **Custom CNN architecture** built from scratch
- **Input:** 48x48 grayscale facial images
- **Layers:** Conv2D, MaxPooling2D, Dropout, Dense, BatchNormalization
- **Data Augmentation:** Applied to reduce overfitting
- **Evaluation:** ~70% validation accuracy, 67% training accuracy
- **Exported Model:** [`Uzair-Emotion_model.h5`](Uzair-Emotion_model.h5)

For full training and architecture details, see [`CNN-7 Type_Emotion_Detection.ipynb`](CNN-7 Type_Emotion_Detection.ipynb).

---

## 🚀 Web App Features

- **Built with Flask** ([`app.py`](app.py))
- **Upload facial images** for emotion detection
- **Backend loads pre-trained CNN model**
- **Real-time emotion prediction**
- **Frontend:** Responsive HTML/CSS ([`templates/index.html`](templates/index.html))

---

## 🛠 Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- Flask
- HTML / CSS (Jinja templates)
- NumPy, Matplotlib,Seaborn

---

## 📊 Evaluation Metrics

- Accuracy
- Confusion Matrix

---

## 🔍 Sample Prediction Flow

1. User uploads a facial image via the web interface.
2. Image is converted to grayscale and resized to 48x48 pixels.
3. Preprocessed image is passed to the CNN model.
4. Model returns the predicted emotion label.
5. Prediction and uploaded image are displayed on the results page.

---

## 💡 Real-World Applications

- Mental health monitoring
- Emotion-aware AI systems
- Social media emotion analysis
- Customer support sentiment detection

---

## 🖼 Example Emotions Recognized

- 😠 **Angry**
- 😖 **Disgust**
- 😨 **Fear**
- 😀 **Happy**
- 😢 **Sad**
- 😲 **Surprise**
- 😐 **Neutral**

---

## 📌 Final Notes

- Model trained from scratch with several architectural iterations.
- Last architecture achieved the best results.
- Entire system tested locally and deployed via Flask for demonstration.

---

## 👨‍💻 Author

**Muhammad Uzair**  
Passionate about Deep Learning, Computer Vision, and real-world AI applications.

---

## 🚦 How to Run Locally

1. **Install dependencies:**
    ```sh
    pip install flask tensorflow numpy opencv-python
    ```
2. **Start the Flask app:**
    ```sh
    python app.py
    ```
3. **Open your browser:**  
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) and upload a facial image to detect its emotion.

---

> For any queries or collaboration, feel free to reach out!