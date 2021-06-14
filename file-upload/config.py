import os


DB_USER = 'root'
DB_PASSWORD = 'heunyam'
DB_HOST = 'localhost'
DB_PORT = 3306
DB_NAME = 'file_upload_test'

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8"

UPLOAD_FOLDER = './uploads'
