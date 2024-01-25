from flask import Flask, Blueprint, render_template, url_for, request, redirect
import sqlite3 as sql


auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
  return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
  name = request.form.get("name")
  email = request.form.get("email")
  password = request.form.get("password")
  
  with sql.connect("example3.db") as con:
    cur = con.cursor()

    sqle = '''
       INSERT INTO tblUsers3(name,email,password) VALUES (?,?,?), (name,email,password)
    '''

    cur.execute(sqle)

    con.commit()
  
  return redirect(url_for("auth.login"))

@auth.route('/login')
def login():
  return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
  email = request.form.get('email')
  password = request.form.get('password')
  print(email, password)
  return redirect(url_for('main.profile'))


@auth.route('/logout')
def logout():
  return "Use this to log out"










