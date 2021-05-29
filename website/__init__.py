from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from .views import views
from .auth import auth


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'j23hrruadaqrj32p29u1ouojalkdjfla4i321wes'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    
    # registering files
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # creating db
    from .models import User, Note
    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app = app)
        print('[+] Created Database!')
