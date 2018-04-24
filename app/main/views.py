from . import main
from flask import render_template


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/docs')
def documentaion():
    return render_template('docs.html')


@main.route('/source')
def source():
    return render_template('source.html')
