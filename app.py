from flask import Flask, render_template, request
import cv2
import numpy as np
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    file = request.files['image']
    if file:
        img_array = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("static/output_gray.jpg", gray)
        edges = cv2.Canny(img, 100, 200)
        cv2.imwrite("static/output_edges.jpg", edges)
        blurred = cv2.GaussianBlur(img, (15, 15), 0)
        cv2.imwrite("static/output_blur.jpg", blurred)
        gray_blur = cv2.medianBlur(gray, 5)
        edges_cartoon = cv2.adaptiveThreshold(
            gray_blur, 255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY, 9, 9
        )
        color = cv2.bilateralFilter(img, d=9, sigmaColor=300, sigmaSpace=300)
        cartoon = cv2.bitwise_and(color, color, mask=edges_cartoon)
        cv2.imwrite("static/output_cartoon.jpg", cartoon)

        return {
            "gray": "static/output_gray.jpg",
            "edges": "static/output_edges.jpg",
            "blur": "static/output_blur.jpg",
            "cartoon": "static/output_cartoon.jpg"
        }

    return "Error", 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # default to 10000 if PORT not set
    app.run(debug=False, host='0.0.0.0', port=port)

