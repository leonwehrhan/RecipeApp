from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class NewRecipeForm(FlaskForm):
    title = StringField('Title',
                        validators=[DataRequired(), Length(min=2, max=100)])
    ingredients = TextAreaField('Ingredients',
                                validators=[DataRequired()])
    spices = StringField('Spices',
                         validators=[Length(max=500)])
    instructions = TextAreaField('Instructions',
                                 validators=[DataRequired()])
    submit = SubmitField('Submit')
