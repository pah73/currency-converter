#This part is not working yet

# web_app/routes/currency_routes.py

from flask import Blueprint, request, jsonify, render_template

#from app.converter import convert
from app.converter import currency_convertor

currency_routes = Blueprint("currency_routes", __name__)

#this is the form where the user will input everything
@currency_routes.route("/currency/form")
def currency_form():
    print("Currency Form...")
    return render_template("currency_form.html")


#this is the route where the output from user inputs are given 
#and the calculation is done, calling converter.py function
@currency_routes.route("/currency/results", methods=["GET", "POST"])
def currency_conversion():
    print("Currency Conversion...")

    #not sure what this does
    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    base_currency = request_data.get("base_currency") or "USD"
    currency_to = request_data.get("currency_to") or "EUR"
    amount = request_data.get("amount") or "10"

    results = currency_convertor(base_currency,currency_to,amount)
    if results:
        # this is where the test notification goes
        return render_template("currency_results.html", base_currency=base_currency,currency_to=currency_to,amount=amount)
    else:
        return redirect("/currency/form")

