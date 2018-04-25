from flask import render_template, redirect, url_for, request, flash
from . import auth
from flask_login import login_user, logout_user, login_required
from ..models import User
from .forms import LoginForm, RegistrationForm
from .. import db
# from ..email import mail_message


@auth.route('/register', methods=["GET", "POST"])
def register():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        user = User(name=registration_form.name.data, email=registration_form.email.data, password=registration_form.password.data)
        db.session.add(user)
        db.session.commit()

        # mail_message("Welcome to Kensus", "email/welcome_user", user.email, user=user)

        return redirect(url_for('auth.success'))
    title = "Register for API key"
    return render_template('auth/register.html', registration_form=registration_form, title=title)


@auth.route('/success')
def success():
    return render_template('auth/success.html')


@auth.route('/account')
def account():
    return render_template('auth/dashboard.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(url_for('main.index'))

        flash('Invalid Email or Password')

    title = "Kensus Login"
    return render_template('auth/login.html', login_form=login_form, title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
