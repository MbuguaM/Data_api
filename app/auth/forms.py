from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, EqualTo, Length
# from ..models import User


class RegistrationForm(FlaskForm):
    name = StringField('First name', validators=[Required(), Length(min=6, max=35)])
    email = StringField('Email ', validators=[Required(), Email(), Length(min=6, max=50)])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message='Passwords must match'), Length(min=6, max=255)])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    recaptcha = RecaptchaField()
    terms = BooleanField('I agree to the terms.', validators=[Required()])
    attribution = BooleanField('I promise to add an attribution link on my website or app to kensusapi.herokuapp.com.', validators=[Required()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email(), Length(min=6, max=50)])
    password = PasswordField('Password', validators=[Required(), Length(min=6, max=255)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Submit')
