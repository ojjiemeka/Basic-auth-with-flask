from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

    
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'emmy'
    
    # Importing the views module from the views package.
    from .views import views
    
    # Importing the auth blueprint from the auth package.
    from .auth import auth
    
    # Registering the views and auth blueprints to the app.
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    # create_database(app)
    
    return app
