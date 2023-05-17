from flask import render_template, url_for, flash, redirect
from recipes import app, db
from recipes.forms import NewRecipeForm
from recipes.models import Recipe


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/new", methods=['GET', 'POST'])
def new():
    form = NewRecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(title=form.title.data,
                        spices='',
                        image='default.jpg',
                        link='',
                        instructions=form.instructions.data)
        db.session.add(recipe)
        db.session.commit()
        flash('New recipe has been submitted', 'success')
        return redirect(url_for('home'))
    return render_template('new_recipe.html', title='New Recipe', form=form)
