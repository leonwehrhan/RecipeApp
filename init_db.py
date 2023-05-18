from recipes import db
from recipes.models import Recipe, Ingredient, RecipeIngredient
import os


if os.path.exists('recipes/site.db'):
    os.remove('recipes/site.db')

db.create_all()

sample_recipe = Recipe()
sample_recipe.title = 'Sample Title'
sample_recipe.instructions = '1. aa bb \n 2. bb cc dd'

for x in ['Potato', 'Salt']:
    a = RecipeIngredient(quantity='1')
    a.ingredient = Ingredient(name=x)
    sample_recipe.ingredients.append(a)

db.session.add(sample_recipe)
db.session.commit()
