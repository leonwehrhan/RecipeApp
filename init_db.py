from recipes import db
from recipes.models import Recipe, Ingredient, RecipeIngredient
from recipes.utils.db_io import parse_ingredients
import os


if os.path.exists('recipes/site.db'):
    os.remove('recipes/site.db')

db.create_all()

sample_recipe = Recipe()
sample_recipe.title = 'Kartoffeln mit Kräuterquark'
sample_recipe.instructions = '1. Kartoffeln in Wasser kochen. 2. Quark mit Schnittlauch und Petersilie, Pfeffer und Salz verrühren. Ggf. Wasser zugeben. Dann Leinöl einrühren.'

for x in parse_ingredients('\n'.join(['1 kg Kartoffeln', '1 kg Quark', 'Schnittlauch', 'Petersilie', 'Salz', 'Pfeffer', 'Leinöl'])):
    a = RecipeIngredient(quantity=x[1], unit=x[2])
    a.ingredient = Ingredient(name=x[0])
    sample_recipe.ingredients.append(a)

db.session.add(sample_recipe)
db.session.commit()
