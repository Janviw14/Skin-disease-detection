# Skin Disease Detection using Flask and TensorFlow

This project demonstrates a skin disease detection system using a pre-trained TensorFlow model deployed with Flask. Users can upload images of skin lesions, and the system will predict the most likely skin disease along with a confidence score.

## Requirements
- Python 3.x
- TensorFlow
- Flask
- NumPy
- PIL (Python Imaging Library)

## Installation
1. Clone the repository:

    ```
    git clone <repository_url>
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage
1. Run the Flask server:

    ```
    python app.py
    ```

2. Open your web browser and navigate to `http://localhost:5000`.

3. Upload an image of a skin lesion using the provided interface.

4. Wait for the system to process the image and display the predicted skin disease along with the confidence score.

## Files Description
- `app.py`: Main Flask application containing routes for uploading images and making predictions.
- `frontend.html`: HTML template for the user interface.
- `model/`: Directory containing the pre-trained TensorFlow model for skin disease detection.
- `static/`: Directory for storing static files such as images.

## How It Works
1. The user uploads an image of a skin lesion through the web interface.
2. The Flask server receives the image and preprocesses it.
3. The pre-trained TensorFlow model is loaded, and the image is passed through the model for prediction.
4. The predicted skin disease class and confidence score are returned to the user interface.

## Customization
- You can replace the pre-trained TensorFlow model with your own trained model by saving it in the `model/` directory and updating the model loading code in `app.py`.
- Modify the HTML template (`frontend.html`) to customize the appearance of the user interface.
