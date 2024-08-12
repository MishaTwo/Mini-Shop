
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=50)])
    phone = StringField("Phone Number", validators=[DataRequired(), Length(max=30)])
    email = StringField("Email", validators=[Email(), DataRequired()])
    passsword = PasswordField("Password", validators=[DataRequired()])
    confirm = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message='Password must be match')])
    submit = SubmitField("Register")