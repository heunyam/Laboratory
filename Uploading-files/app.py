from flask import Flask, request
from werkzeug.utils import secure_filename

import os, boto3


# DB_USER = 'root'
# DB_PASSWORD = 'heunyam'
# DB_HOST = 'localhost'
# DB_PORT = 3306
# DB_NAME = 'file_upload_test'
# DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8"

S3_BUCKET = ""
S3_ACCESS_KEY = ""
S3_SECRET_ACCESS = ""
S3_BUCKET_URL = f""

app = Flask(__name__)
s3 = boto3.client(service_name='s3', aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_ACCESS, region_name='ap-northeast-2')


@app.route('/picture', methods=['POST'])
def upload_picture():

    if 'image' not in request.files:
        return 'Cannot find image', 404
    # 이러면 request key 값을 image로 보내야함

    image = request.files['image']

    if image.filename == '':
        return 'Cannot find image filename', 404

    filename = secure_filename(image.filename)
    s3.upload_fileobj(image, S3_BUCKET, filename)
    image_url = f"{S3_BUCKET_URL}{filename}"

    return image_url


def save_picture(picture, filename):

    s3.upload_fileobj(picture, S3_BUCKET, filename)

    return f"{S3_BUCKET_URL}{picture.filename}"
