from recipes import db


class RecipeIngredient(db.Model):
    __tablename__ = 'recipeingredient'
    id = db.Column(db.Integer, primary_key=True, index=True)
    recipeId = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    ingredientId = db.Column(db.Integer, db.ForeignKey('ingredient.id'))

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    # spices = db.Column(db.String(500))
    instructions = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    link = db.Column(db.String(100))
    #ingredients = db.relationship('Ingredient', secondary=RecipeIngredient.__table__, backref='recipes')
    ingredients = db.Column(db.Text, nullable=False)


class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(8), nullable=False)
    ingredient = db.relationship('Recipe', secondary=RecipeIngredient.__table__, backref='ingredient')


def init_db():
    db.create_all()

    sample_recipe = Recipe('Sample Recipe', '1. aa bb\n 2. bb cc', 'default.jpg', '', 'Potato\nSalt\nPepper')
    db.session.add(sample_recipe)
    db.session.commit()


if __name__ == '__main__':
    init_db()