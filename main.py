from flask import Flask, Blueprint, render_template
from auth import auth
from flask_sqlalchemy import SQLAlchemy


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def index():
  return render_template('index.html')

@main.route('/profile')
def profile():
  return render_template('profile.html')



app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(auth)
app.run(host='0.0.0.0', port=8080)

