from . import main
from flask import render_template, jsonify, request
import json

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


@main.route('/endpoints')
def endpoints():
    title = "Endpoints"
    return render_template('docs/endpoints.html', title=title)


@main.route('/pricing')
def pricing():
    return render_template('pricing.html')


@main.route('/errors')
def errors():
    title = "Error"
    return render_template('docs/errors.html', title=title)


@main.route('/source')
def source():
    title = "Sources"
    return render_template('source.html', title=title)


@main.route('/terms')
def terms():
    return render_template('terms.html')


# api endpoints
@main.route('/Everything', methods=['GET'])
def test_activities():
    everything = [{"activities": loaded_activities}, {'population': loaded_population}, {'areas': loaded_areas}, {'internet': loaded_internet}, {'materials': loaded_internet}]
    return jsonify({'all': everything})


@main.route('/Everthing/<name>', methods=['Get'])
def test_population(name):
    everything = [{'key': "activities", 'info': loaded_activities}, {'key': 'population', 'info': loaded_population}, {'key': 'areas', 'info': loaded_areas}, {'key': 'internet', 'info': loaded_internet}, {'key': 'materials', 'info': loaded_internet}]

    for detail in everything:
            if detail.get('key') == name:
                return jsonify(detail)

    return jsonify({'message': 'bad request'})
