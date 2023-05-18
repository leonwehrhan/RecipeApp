from recipes import db


class RecipeIngredient(db.Model):
    __tablename__ = 'recipeingredient'
    id = db.Column(db.Integer, primary_key=True, index=True)
    recipeId = db.Column(db.Integer, db.ForeignKey('recipe_table.id'))
    ingredientId = db.Column(db.Integer, db.ForeignKey('ingredient_table.id'))

    quantity = db.Column(db.Float)
    unit = db.Column(db.String(8))

    recipe = db.relationship('Recipe', back_populates='ingredients')
    ingredient = db.relationship('Ingredient', back_populates='recipes')

class Recipe(db.Model):
    __tablename__ = 'recipe_table'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    # spices = db.Column(db.String(500))
    instructions = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20))
    link = db.Column(db.String(100))
    ingredients = db.relationship('RecipeIngredient', back_populates='recipe')


class Ingredient(db.Model):
    __tablename__ = 'ingredient_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    recipes = db.relationship('RecipeIngredient', back_populates='ingredient')


class Unit(db.Model):
    __tablename__ = 'units'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
