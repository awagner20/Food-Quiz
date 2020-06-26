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
    if Salad > top_food:
        top_food = Salad
        top_word = 'Salad'
    if top_word == 'Pasta':
        image_link = "https://pinchofyum.com/wp-content/uploads/Vegan-Vodka-Pasta-Square.jpg"
    if top_word == "Ramen":
        image_link = "https://hips.hearstapps.com/hmg-prod/images/190208-delish-ramen-horizontal-093-1550096715.jpg"
    if top_word == "Salad":
        image_link = "https://www.olivetomato.com/wp-content/uploads/2019/12/Green-salad-with-feta.jpeg"
    if top_word == "Steak":
        image_link = "https://i.ytimg.com/vi/nsw0Px-Pho8/maxresdefault.jpg"
    if top_word == "Sandwiches":
        image_link = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/190322-ham-sandwich-horizontal-1553721016.png"
    if top_word == "Sushi":
        image_link = "https://res.cloudinary.com/tf-lab/image/upload/w_656,h_368,c_fill,g_auto:subject,q_auto,f_auto/restaurant/b4e95a93-b6f6-4a16-a642-358a87c8d0b3/d368dfe4-68b1-4e1e-bd2b-7c917ed6824a.jpg"
    return render_template('results.html', top_word = top_word, image_link = image_link, time=datetime.now())

