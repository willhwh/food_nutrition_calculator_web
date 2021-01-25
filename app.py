from flask import Flask, request, redirect, render_template, url_for
from parse_realtive import static
from class_folder.inputs_class import Inputs



app = Flask(__name__)

# GET — used to send data back only
# POST — used to receive data

global user
user = ''
global restaurant
restaurant = ''
global restaurant_name
restaurant_name = ''
global meal_name
meal_name = ''
global select_meal
select_meal = ''


@app.route('/', methods=['GET', 'POST'])
def user_page():
        if request.method == 'POST': 
            return redirect(url_for("login_page"))
            
        else:
            return render_template("index.html")


@app.route('/login', methods=['GET', 'POST']) 
def login_page():
    if request.method == 'POST': 
        user = request.values['username']
        return redirect(url_for("home_page",user=user))
    else:
       return render_template("login.html")
    

@app.route('/home/<user>', methods=['GET', 'POST']) 
def home_page(user):
    if request.method == 'GET': #get data from previous redirect page (login_page)
        return render_template("home.html", user = user) 

    if request.method == 'POST':
        target_calories = request.values['target_calories']
        target_proteins = request.values['target_proteins']
        target_fat = request.values['target_fat']
        target_carbs = request.values['target_carbs']
        print( target_calories, target_proteins, target_fat, target_carbs)
        return redirect(url_for("food_page"))


@app.route('/food',methods=['GET', 'POST'])
def food_page():
    if request.method == 'GET':
        return render_template("food.html")

    if request.method == 'POST':
        restaurant = request.values['restaurant']
        web_url, driver = static()
        global user_input
        user_input = Inputs(web_url,driver)
        restaurant_name = user_input.get_restaurant_name(restaurant)
        return redirect(url_for("food_brand_page",restaurant_name = restaurant_name))


@app.route('/food_brand/<restaurant_name>',methods=['GET', 'POST'])
def food_brand_page(restaurant_name):
    if request.method == 'GET':
        return render_template("food_brand.html",restaurant_name = restaurant_name) 

    if request.method == 'POST':
        check = request.values['check_tf']
        if check == 'Yes':
            print(restaurant_name)
            select_restaurant = request.values['select_restaurant']
            return redirect (url_for("food_branded_page",restaurant_name = select_restaurant))
        else:
            return redirect(url_for("food_page"))

@app.route('/food_branded/<restaurant_name>',methods=['GET', 'POST'])
def food_branded_page(restaurant_name):
    if request.method == 'GET':
        return render_template("food_branded.html",restaurant_name=restaurant_name) 

    if request.method == 'POST':
        select_restaurant =  request.values['select_restaurant']
        meal = request.values['meal']
        global user_input
        meal_names = user_input.get_meal_name(meal)
        return redirect(url_for("food_meal_page",select_restaurant=select_restaurant,meal_names = meal_names))

@app.route('/food_meal/<select_restaurant>/<meal_names>',methods=['GET', 'POST'])
def food_meal_page(select_restaurant, meal_names):
    if request.method == 'GET':
        return render_template('food_meal.html',select_restaurant=select_restaurant,meal_names = meal_names)
    
    if request.method == 'POST':
        select_meal = request.values['select_meal']
        select_restaurant =  request.values['select_restaurant']
        print(select_meal)
        print(select_restaurant)
        global user_input
        calories, fat, carbs, proteins = user_input.get_meal_info(select_restaurant,select_meal)

        return redirect(url_for('food_mealed_page',select_restaurant=select_restaurant,select_meal = select_meal,\
            calories=calories, fat=fat, carbs=carbs, proteins=proteins))

@app.route('/food_mealed/<select_restaurant>/<select_meal>/<calories>/<fat>/<carbs>/<proteins>',methods=['GET', 'POST'])
def food_mealed_page(select_restaurant,select_meal,calories,fat,carbs,proteins):
    if request.method == 'GET':
        print(select_restaurant)
        print(select_meal)
        return render_template('food_mealed.html',select_restaurant=select_restaurant,select_meal = select_meal,\
            calories=calories, fat=fat, carbs=carbs, proteins=proteins)
    
    if request.method == 'POST':
       print("Back to Food_Page")
       return redirect(url_for('food_page'))
   




@app.route('/charts',methods=['GET', 'POST'])
def chart_page():
    return render_template("chart.html")





if __name__ == '__main__':
    app.debug = True
    app.run()    