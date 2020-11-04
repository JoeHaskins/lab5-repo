import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that has my Bio
    @app.route('/')
    def hello():
        return 'Welcome to my webpage. My name is Joe haskins and I am a third year computer science student. I grew up on a farm and I own a cat with my girlfriend called Kiki'
    @app.route('/contact-me')
    def email():
        return 'Hello, World!'
    return app
