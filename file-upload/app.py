import os

from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
# app.config.from_pyfile('./config.py')


@app.route('/ping')
def ping():
    return 'pong', 200


@app.route('/upload', methods=['POST'])
def upload_image():

    if 'image' not in request.files:
        return 'Cannot find image', 404
    # 이러면 request key 값을 image로 보내야함

    image = request.files['image']

    if image.filename == '':
        return 'Cannot find image filename', 404

    filename = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return '', 200


