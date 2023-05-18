from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from recipes import secret_key


app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key.get_secret_key()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from recipes import routes
