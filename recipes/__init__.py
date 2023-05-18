from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from secret_key import get_secret_key


app = Flask(__name__)
app.config['SECRET_KEY'] = get_secret_key()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from recipes import routes
