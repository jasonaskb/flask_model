from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_marshmallow import Marshmallow
import os


# app is the current Flask app that we're using.
app = Flask(__name__)


# Creating an endpoint for the route
@app.route('/')
def home():
    return jsonify(data='Welcome to my flask api home')


# Python scripts have the value '__main__' when being executed (not imported)
if __name__ == '__main__':  # This line of code is very common in production code
    app.run(host='0.0.0.0')