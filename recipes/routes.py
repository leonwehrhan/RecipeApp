from flask import render_template
from recipes import app
from recipes.forms import NewRecipeForm


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/new", methods=['GET', 'POST'])
def new():
    form = NewRecipeForm()
    return render_template('new_recipe.html', title='New', form=form)
