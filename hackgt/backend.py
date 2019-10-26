from flask import Flask, jsonify, request
from PIL import Image
import pytesseract
import argparse
import os
import cv2

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'

@app.route('/home', methods=['POST'])
def home():
    data = request.files['file']
    return jsonify({"status":"ok"})

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
# text = pytesseract.image_to_string(Image.open(filename))
# os.remove(filename)
# print(text)

if __name__ == '__main__':
    app.run(port=8000)