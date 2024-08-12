from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, FileField, SubmitField
from wtforms.validators import DataRequired, Length

class AddItemForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired(), Length(max=50)])
    category = StringField("Category: ", validators=[DataRequired(), Length(max=50)])
    price = StringField("Price: ", validators=[DataRequired()])
    details = StringField("Price: ", validators=[DataRequired()])
    price_id = StringField("Price_id: ", validators=[DataRequired()])
    image = FileField("Image", validators=[DataRequired()])
    submit = SubmitField("Add")