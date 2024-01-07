import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from flask import Flask, request, render_template, jsonify
from PIL import Image

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('frontend.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    if file:
        file_path = r"C:\Users\Nivedh\Dropbox\PC\Desktop\model\blood\static\image.png"
        file.save(file_path)
        data = []
        model_save_location = r'C:\Users\Nivedh\Dropbox\PC\Desktop\model\model'
        image_path = file_path
        loaded_model = tf.saved_model.load(model_save_location)
        # Load and preprocess the image
        img = image.load_img(image_path, target_size=(128, 128))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0
        # Make predictions
        predictions = loaded_model(img_array)
        predicted_class = np.argmax(predictions)
        max_confidence = np.max(predictions)
        print(predictions)
        file_path ="\static\image.png"
        data.append({"predicted_class": int(predicted_class), "max_confidence": float(max_confidence*100)})
        return jsonify(data=data, image_path=file_path)    
    
@app.route('/scrape_data', methods=['POST'])
def predict():
    data = []
    model_save_location = r'C:\Users\Nivedh\Dropbox\PC\Desktop\model\model'
    image_path = r"C:\Users\Nivedh\Dropbox\PC\Desktop\model\blood\processed_image.png"
    loaded_model = tf.saved_model.load(model_save_location)

    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Make predictions
    predictions = loaded_model(img_array)
    predicted_class = np.argmax(predictions)
    max_confidence = np.max(predictions)
    print(predicted_class)
    print(max_confidence)
    data.append({"predicted_class": int(predicted_class), "max_confidence": float(max_confidence*100)})
    return jsonify(data=data)

if __name__ == '__main__':
    app.run(debug=True)

