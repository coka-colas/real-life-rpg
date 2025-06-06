from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rpg.db'
app.config['SECRET_KEY'] = 'supersecretkey'

db = SQLAlchemy(app)

from app import models
from app import routes
