import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import json


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/hello')
def hello_world():
    return "hello world"


@app.route('/')
def index():
    return "this is a index page"


@app.route('/user/<username>')
def show_user(username):
    return 'username is: %s' % username


@app.route('/login', methods=['GET', 'POST'])
def get():
    if request.method == 'GET':
        return 'this is a get'
    else:
        username = request.args.get('username')
        return 'username is {}'.format(username)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            basepath = os.path.dirname(__file__)
            uploadpath = os.path.join(basepath, app.config['UPLOAD_FOLDER'], filename)
            print('basepath:' + uploadpath)
            f.save(uploadpath)
            downpath = load_uploadpic(uploadpath, filename)
            print('downloadpath:' + downpath)
            return jsonify({'filename': f.filename, 'uploadpath': uploadpath, 'downloadpath': downpath, })


if __name__ == '__main__':
    app.run()
