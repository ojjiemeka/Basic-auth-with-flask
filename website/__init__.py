from flask import Flask

def create_app():
    app = flask(__name__)
    app.config['SECRET_KEY'] = 'emmy'
    
    return app