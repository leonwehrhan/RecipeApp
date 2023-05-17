from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '53988888f0b3dbcfa810237ab0bdc2b2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from recipes import routes
