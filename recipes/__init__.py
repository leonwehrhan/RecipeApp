from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '53988888f0b3dbcfa810237ab0bdc2b2'

from recipes import routes
