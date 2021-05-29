from flask import Flask
from flask_sqlalchemy import SQLALchemy
from .views import views
from .auth import auth

db = SQLALchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'j23hrruadaqrj32p29u1ouojalkdjfla4i321wes'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    
    # registering files
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
