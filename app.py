# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
# -- Initialization section --
app = Flask(__name__)
# Point totals should all be around 15 by the end of the quiz
# Hamburgers = 0
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    print(datetime.now())
    return render_template('index.html', time=datetime.now())

@app.route('/sendFood', methods=['GET','POST'])
def quiz():
    Pasta = 0
    Ramen = 0
    Sushi = 0
    Steak = 0
    Sandwiches = 0
    Salad = 0
    choice1 = request.form["spice"] 
    choice2 = request.form["drink"]
    choice3 = request.form["travel"]
    choice4 = request.form["important"]
    choice5 = request.form["flavor"]
    # CHOICE 1
    if choice1 == "salt":
        Ramen = Ramen + 2
        Steak = Steak + 1
        Sandwiches = Sandwiches + 1
    elif choice1 == 'no spice':
        Sushi = Sushi + 2
        Pasta = Pasta + 2
    elif choice1 == 'pepper':
        Steak = Steak + 2
        Ramen = Ramen + 1
        Salad = Salad + 1
    #CHOICE 2
    if choice2 == "coke":
        Ramen = Ramen + 2
        Sushi = Sushi + 1
    if choice2 == "champagne":
        Steak = Steak + 2
        Pasta = Pasta + 1
    if choice2 == "water":
        Sushi = Sushi + 2
        Pasta = Pasta + 1
        Salad = Salad + 2
        Sandwiches = Sandwiches + 1
    #CHOICE 3
    if choice3 == "texas":
        Steak = Steak + 3
    if choice3 == "no where":
        Sandwiches = Sandwiches + 4
        Salad = Salad + 1
    if choice3 == "italy":
        Pasta = Pasta + 3
        Salad = Salad + 1
    if choice3 == "japan":
        Sushi = Sushi + 4
        Ramen = Ramen + 3
    # CHOICE 4
    if choice4 == "cheap":
        Sandwiches = Sandwiches + 2
        Pasta = Pasta + 1
        Salad = Salad + 2
        Steak = Steak - 1
    if choice4 == "healthy":
        Ramen = Ramen - 1
        Steak = Steak - 1
        Sandwiches = Sandwiches + 2
        Salad = Salad + 3
        Pasta = Pasta + 1
    if choice4 == "flavorful":
        Steak = Steak + 3
        Ramen = Ramen + 2
        Sandwiches = Sandwiches - 1
    if choice4 == "filling":
        Ramen = Ramen + 1
        Pasta = Pasta + 2
        Salad = Salad - 1
    # CHOICE 5
    if choice5 == "salty":
        Ramen = Ramen + 2
        Steak = Steak + 1
    if choice5 == "sweet":
        Sushi = Sushi + 1
    if choice5 == "sour":
        Ramen = Ramen + 1
        Pasta = Pasta + 1
    if choice5 == "bitter":
        Sandwiches = Sandwiches + 1
        Salad = Salad + 2
    top_food = 0
    top_word = ""
    if Pasta > top_food:
        top_food = Pasta
        top_word = 'Pasta'
    if Ramen > top_food:
        top_food = Ramen
        top_word = 'Ramen'
    if Sushi > top_food:
        top_food = Sushi
        top_word = 'Sushi'
    if Steak > top_food:
        top_food = Steak
        top_word = 'Steak'
    if Sandwiches > top_food:
        top_food = Sandwiches
        top_word = 'Sandwiches'
    return render_template('results.html', top_word = top_word)