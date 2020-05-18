import os

BASE_DIR = os.getcwd()

DEBUG = True
HOST = 'localhost'
PORT = 8080

PRODUCT_URL = 'https://xxx.com'  # まだ本番環境の想定がないので, とりあえず
if DEBUG:
    PRODUCT_URL = 'http://localhost:8080'
