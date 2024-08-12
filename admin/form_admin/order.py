from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, FileField, SubmitField
from wtforms.validators import DataRequired, Length

class OrderEditForm(FlaskForm):
    status = StringField("Status:", validators=[DataRequired()])
    submit = SubmitField("Add")