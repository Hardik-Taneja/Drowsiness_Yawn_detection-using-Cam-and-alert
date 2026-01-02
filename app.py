from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64
from detector import analyze_frame
DEPLOY_MODE = True

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if DEPLOY_MODE:
        # Mock response for demo
        return jsonify({"status": "SAFE"})
    data = request.json["image"]
    img_bytes = base64.b64decode(data.split(",")[1])
    img_array = np.frombuffer(img_bytes, np.uint8)
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    status = analyze_frame(frame)
    return jsonify({"status": status})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
