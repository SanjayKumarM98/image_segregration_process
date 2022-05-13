#importing libraries

import os
from flask import Flask,flash,request,Response,jsonify,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

#Creating an instance of the flask app
app=Flask(__name__)

#Configure our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://sanjay:password@localhost/students'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER='/home/divum/PycharmProjects/flask_crud_practice/'
ALLOWED_EXTENSIONS={'csv'}

app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
