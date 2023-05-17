from recipes import db
from recipes.models import Recipe
import os


if os.path.exists('recipes/site.db'):
    os.remove('recipes/site.db')
    db.create_all()

    sample_recipe = Recipe()
    sample_recipe.title = 'Sample Title'
    sample_recipe.instructions = '1. aa bb \n 2. bb cc dd'
    sample_recipe.image = ''
    sample_recipe.link = ''
    sample_recipe.ingredients = 'Potato \n Salt \n Pepper'
    db.session.add(sample_recipe)
    db.session.commit()
else:
    db.create_all()