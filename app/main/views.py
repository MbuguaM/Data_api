from . import main
from flask import render_template, jsonify, request
import json


@main.route('/')
def index():
    title = "Kensus API"
    return render_template('index.html', title=title)


@main.route('/docs')
def documentation():
    title = "Documentation"
    return render_template('docs/docs.html', title=title)


@main.route('/auth')
def Authentication():
    title = "Authentication"
    return render_template('docs/auth.html', title=title)


@main.route('/clientlib')
def clientlib():
    title = "Client Libraries"
    return render_template('docs/clientlib.html', title=title)

@main.route('/activities',methods = ['Get'])
def test_activities():
    return jsonify({"activities" : loaded_activities})

@main.route('/endpoints')
def endpoints():
    title = "Endpoints"
    return render_template('docs/endpoints.html', title=title)


@main.route('/errors')
def errors():
    title = "Error"
    return render_template('docs/errors.html', title=title)


@main.route('/source')
def source():
    title = "Sources"
    return render_template('source.html', title=title)

@main.route('/population',methods = ['Get'])
def test_population():
    return jsonify({"activities" : loaded_population})

@main.route('/terms')
def terms():
    return render_template('terms.html')


@main.route('/pricing')
def pricing():
    return render_template('pricing.html')
