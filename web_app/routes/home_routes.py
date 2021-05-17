# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template
from app.convertor import currency_options

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT The Currency Converter app:...")
    return render_template("about.html")

@home_routes.route("/options")
def hello_world():

    currency_list = currency_options()

    print("Options...", dict(request.args))
    # NOTE: `request.args` is dict-like, so below we're using the dictionary's `get()` method,
    # ... which will return None instead of throwing an error if key is not present
    # ... see also: https://www.w3schools.com/python/ref_dictionary_get.asp
    
    return render_template("options.html", currency_list=currency_list)
    

    