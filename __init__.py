from flask import Flask
from flask_sqlalchemy import SQLAlchemy


_db = SQLAlchemy()

def create_app():
  app = Flask(__name__)

  app.config['SECRET_KEY'] = "random string"
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jello.db'

  _db.init_app(app)

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  
  return app