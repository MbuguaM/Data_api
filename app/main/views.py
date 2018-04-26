from . import main
from flask import render_template,jsonify,request
import json

# open the json files 
Activities = open("app/data/parsed_activity.json","r")
areas = open("app/data/parsed_areas.json","r")
internet = open ("app/data/parsed_internet.json","r")
materials = open ("app/data/parsed_materials.json","r")
population = open ("app/data/parsed_population.json","r")

# load the information into list 
loaded_activities = json.load(Activities)
loaded_areas = json.load(areas)
loaded_internet = json.load(internet)
loaded_materials = json.load(materials)
loaded_population = json.load(population)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/docs')
def documentaion():
    return render_template('docs.html')


@main.route('/source')
def source():
    return render_template('source.html')

@main.route('/activities',methods = ['Get'])
def test_activities():
    return jsonify({"activities" : loaded_activities})

@main.route('/areas',methods = ['Get'])
def test_areas():
    return jsonify({"activities" : loaded_areas})

@main.route('/internet',methods = ['Get'])
def test_internet():
    return jsonify({"activities" : loaded_internet})

@main.route('/materials',methods = ['Get'])
def test_materials():
    return jsonify({"activities" : loaded_materials})

@main.route('/population',methods = ['Get'])
def test_population():
    return jsonify({"activities" : loaded_population})

@main.route('/terms')
def terms():
    return render_template('terms.html')
