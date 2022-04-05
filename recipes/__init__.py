from flask import Flask


app = Flask(__name__)

from recipes import routes
