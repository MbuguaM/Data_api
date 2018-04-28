from flask import render_template, redirect, url_for, request, flash, jsonify
from . import auth
from flask_login import login_user, logout_user, login_required
from ..models import User
from .forms import LoginForm, RegistrationForm
from .. import db
from config import Config
import json
import uuid
# from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
# from ..email import mail_message

parsed_activities = open('app/data/parsed_activity.json', 'r')
parsed_population = open('app/data/parsed_population.json', 'r')
parsed_areas = open('app/data/parsed_areas.json', 'r')
parsed_materials = open('app/data/parsed_materials.json', 'r')
parsed_internet = open('app/data/parsed_internet.json', 'r')

loaded_activities = json.load(parsed_activities)
loaded_population = json.load(parsed_population)
loaded_areas = json.load(parsed_areas)
loaded_materials = json.load(parsed_materials)
loaded_internet = json.load(parsed_internet)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'api-access-token' in request.args:
            token = request.args['api-access-token']
        if not token:
            return jsonify({'message': 'token is missing'}), 401
        # try:
        #     data = jwt.decode(token, Config['ENCODE_KEY'])
        #     current_user = User.query.filter_by(public_uid=data['public_uid']).first()
        # except:
        #     return jsonify({'message', 'token is invalid'}), 401
        return f(token, *args, **kwargs)
    return decorated


@auth.route('/register', methods=["GET", "POST"])
def register():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        user = User(public_uid=str(uuid.uuid4()), name=registration_form.name.data, email=registration_form.email.data, password=registration_form.password.data)
        db.session.add(user)
        db.session.commit()

        # mail_message("Welcome to Kensus", "email/welcome_user", user.email, user=user)

        return redirect(url_for('auth.login'))
    title = "Register for API key"
    return render_template('auth/register.html', registration_form=registration_form, title=title)


@auth.route('/success')
def success():
    title = "Success"
    return render_template('auth/success.html', title=title)


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
            # token = jwt.encode({'public_uid': user.public_uid, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=600)}, Config['ENCODE_KEY'])
            # Token = token.decode('UTF-8')
            return redirect(url_for('auth.success'))  #, Token=Token))

        flash('Invalid Email or Password')

    title = "Kensus Login"
    return render_template('auth/login.html', login_form=login_form, title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


# api endpoints
# all the infomation
@auth.route('/Everything', methods=['GET'])
@token_required
def test_activities(token):
    if  token:
        everything = [{"Activities/Occupation": loaded_activities}, {'Population': loaded_population}, {'Areas': loaded_areas}, {'Internet_usage': loaded_internet}, {'Roof_materials': loaded_internet}]
        return jsonify({'all': everything})
    else:
        return jsonify({'message': 'no token'})


# information based on category
@auth.route('/Everything/<name>', methods=['GET'])
@token_required
def activities(token,name):
    if token:
        everything = [{'key': "activities", 'Activities/Occupation': loaded_activities}, {'key': 'population', 'Population': loaded_population}, {'key': 'areas', 'Area': loaded_areas}, {'key': 'internet', 'internet_usage': loaded_internet}, {'key': 'materials', 'Roof_materials': loaded_materials}]

        for detail in everything:
            if detail.get('key') == name:
                return jsonify(detail)
        return jsonify({'message': 'bad requests'})
    else:
        return jsonify({'message': 'no token'})



# infomation based  on county info
@auth.route('/County/<name>', methods=['GET'])
@token_required
def county_info(token,name):
    if token:
        def get_all():
            dicts = []
            # activities
            for detail in loaded_activities:
                if detail.get('county') == name:
                    dicts.append({"Activities/Occupation": detail})
            # loaded_population
            for detail2 in loaded_population:
                if detail2.get('county') == name:
                    dicts.append({'Population': detail2})
            # areas
            for detail3 in loaded_areas:
                if detail3.get('county') == name:
                    dicts.append({'Area': detail3})
            # internet
            for detail4 in loaded_internet:
                if detail4.get('county') == name:
                    dicts.append({'Internet_usage': detail4})
            # roof loaded_materials
            for detail5 in loaded_materials:
                if detail5.get('county') == name:
                    dicts.append({'Roof_materials': detail5})
            return dicts
        all = get_all()
        if all is not None:
            return jsonify({"info": all})

        return jsonify({'message': 'bad requests'})
    else:
        return jsonify({'message': 'no token'})
