from flask import render_template, url_for, flash, redirect
from recipes import app, db
from recipes.forms import NewRecipeForm
from recipes.models import Recipe


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', recipes=Recipe.query.all())


@app.route("/new", methods=['GET', 'POST'])
def new():
    form = NewRecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(title=form.title.data,
                        image='default.jpg',
                        instructions=form.instructions.data,
                        ingredients=form.ingredients.data)
        db.session.add(recipe)
        db.session.commit()
        flash('New recipe has been submitted', 'success')
        return redirect(url_for('home'))
    return render_template('new_recipe.html', title='New Recipe', form=form)
