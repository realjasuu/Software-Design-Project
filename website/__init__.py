from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


def create_app():
    app = Flask(__name__)
    # adding database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Jlcm0907192001J@localhost/mozarstore'
    app.config['SECRET_KEY'] = 'jasonleomozar'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app