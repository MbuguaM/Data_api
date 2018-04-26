from . import main
from flask import render_template, jsonify, request
import json


@main.route('/')
def index():
    title = "Kensus API"
    return render_template('index.html', title=title)


@main.route('/docs')
def documentation():
    return render_template('docs/docs.html')


@main.route('/auth')
def Authentication():
    return render_template('docs/auth.html')


@main.route('/clientlib')
def clientlib():
    return render_template('docs/clientlib.html')

@main.route('/activities',methods = ['Get'])
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
    return jsonify({"activities" : loaded_population})

@main.route('/terms')
def terms():
    return render_template('terms.html')


@main.route('/pricing')
def pricing():
    return render_template('pricing.html')
