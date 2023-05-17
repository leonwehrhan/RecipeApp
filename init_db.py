from recipes import db
import os


if os.path.exists('recipes/site.db'):
    os.remove('recipes/site.db')
    db.create_all()
else:
    db.create_all()