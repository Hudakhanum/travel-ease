from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Create the Flask app
app = Flask(__name__)

# Path to SQLite DB
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'travel.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect SQLAlchemy to Flask app
db = SQLAlchemy(app)

from app import routes  # Import routes after app & db are set
