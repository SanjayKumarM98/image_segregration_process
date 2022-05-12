#importing libraries
from flask import Flask,request,Response,jsonify,url_for,redirect
from flask_sqlalchemy import SQLAlchemy

#Creating an instance of the flask app
app=Flask(__name__)

#Configure our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students_info.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
