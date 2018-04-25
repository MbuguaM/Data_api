from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, EqualTo
# from ..models import User


class RegistrationForm(FlaskForm):
    name = StringField('First name', validators=[Required()])
    email = StringField('Email ', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    recaptcha = RecaptchaField()
    terms = BooleanField('I agree to the terms')
    attribution = BooleanField('I promise to add an attribution link on my website or app to kensusapi.herokuapp.com.')
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Submit')
