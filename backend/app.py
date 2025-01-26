from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from ultralytics import YOLO
import cv2
import numpy as np
from io import BytesIO
from PIL import Image

app = Flask(__name__)
CORS(app) 

# Load YOLO model
model = YOLO("backend/yolo_model.pt") 

@app.route("/predict", methods=["POST"])
def predict_and_send():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files["image"]

    try:
        file_bytes = np.frombuffer(image_file.read(), np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        results = model(image)


        plotted_image = results[0].plot()


        _, buffer = cv2.imencode(".jpg", plotted_image)
        io_buffer = BytesIO(buffer)


        io_buffer.seek(0)
        return send_file(io_buffer, mimetype="image/jpeg")

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": "An error occurred during prediction"}), 500

if __name__ == "__main__":
    app.run(debug=True)
