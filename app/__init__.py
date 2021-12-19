# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask
from app.config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from app.base.routes import base_blueprint
    from app.home.routes import home_blueprint
    from app.home.routes import dieren_blueprint
    from app.home.routes import verblijven_blueprint
    from app.home.routes import users_blueprint
    app.register_blueprint(base_blueprint)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(dieren_blueprint)
    app.register_blueprint(verblijven_blueprint)
    app.register_blueprint(users_blueprint)
    return app
