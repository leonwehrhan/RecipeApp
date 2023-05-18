from flask import render_template, url_for, flash, redirect
from recipes import app, db
from recipes.forms import NewRecipeForm
from recipes.models import Recipe, Ingredient, RecipeIngredient
from .utils.db_io import parse_ingredients


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', recipes=Recipe.query.all())


@app.route("/new", methods=['GET', 'POST'])
def new():
    form = NewRecipeForm()
    if form.validate_on_submit():

        # get ingredients data from the form
        ingredients = form.ingredients.data
        ingredients_list = parse_ingredients(ingredients)

        # make recipe object
        r = Recipe(title=form.title.data,
                   instructions=form.instructions.data)

        # for every list item make association object
        # then append ingredient via association
        for x in ingredients_list:
            name = x[0]
            quantity = x[1]
            unit =x [2]

            a = RecipeIngredient(quantity=quantity, unit=unit)
            a.ingredient = Ingredient(name=name)
            r.ingredients.append(a)
        
        db.session.add(r)
        db.session.commit()

        flash('New recipe has been submitted', 'success')
        return redirect(url_for('home'))
    return render_template('new_recipe.html', title='New Recipe', form=form)
