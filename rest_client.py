from flask import Flask, request, jsonify
from info import GetInfo
from reader import Reader
from PIL import Image
import os
import cv2

app = Flask(__name__)

@app.route('/post-image', methods=['POST'])
def post_image():
    filename = "{}.png".format(os.getpid())
    request.files['file'].save(filename)

    ocr = Reader(filename, '')
    text = ocr.get_text()

    data = GetInfo(text)
    print(data.get_date())
    print(data.get_store())
    print(data.get_total())
    return jsonify({'store': data.get_store(), 'date': data.get_date(), 'total': data.get_total()}), 200

if __name__ == '__main__':
    app.run(debug=True)