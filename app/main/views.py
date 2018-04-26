from . import main
from flask import render_template, jsonify, request
import json

parsed_activities = open('app/data/parsed_activity.json','r')
parsed_population = open('app/data/parsed_population.json','r')

loaded_activities = json.load(parsed_activities)
loaded_population = json.load(parsed_population)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/docs')
def documentation():
    return render_template('docs/docs.html')


@main.route('/auth')
def Authentication():
    return render_template('docs/auth.html')


@main.route('/clientlib')
def clientlib():
    return render_template('docs/clientlib.html')

@main.route('/activities',methods = ['GET'])
def test_activities():
    return jsonify({"activities" : loaded_activities})

@main.route('/endpoints')
def endpoints():
    return render_template('docs/endpoints.html')


@main.route('/errors')
def errors():
    return render_template('docs/errors.html')


@main.route('/source')
def source():
    return render_template('source.html')

@main.route('/population',methods = ['Get'])
def test_population():
    return jsonify({"Population" : loaded_population})

@main.route('/terms')
def terms():
    return render_template('terms.html')


@main.route('/pricing')
def pricing():
    return render_template('pricing.html')
