from flask import Flask, render_template, request, redirect, url_for, session
import os

from web_app.settings import DEBUG, HOST, PORT, BASE_DIR

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'web_app', 'templates'),
    static_folder=os.path.join(BASE_DIR, 'web_app', 'static'),
)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=DEBUG,
        host=HOST,
        port=PORT
    )
