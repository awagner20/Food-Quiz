# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
# -- Initialization section --
app = Flask(__name__)
Pasta = 0
Ramen = 0
Sushi = 0
Steak = 0
# Sandwiches = 0
# Salad = 0
# Hamburgers = 0
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    print(datetime.now())
    return render_template('index.html', time=datetime.now())
@app.route('/sendFood', methods=['GET','POST'])
def quiz():
    choice1 = request.form["spice"] 
    if choice1 == "salt":
        print()
    elif choice1 == 'paprika':
        print()
    elif choice1 == 'pepper':
        return 'Test'
# @app.route('/sendFood', methods=['GET','POST'])
# def results():
#     return 'hello there '