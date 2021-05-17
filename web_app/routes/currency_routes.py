#This part is not working yet

# web_app/routes/currency_routes.py

from flask import Blueprint, request, jsonify, render_template, flash, redirect

#from app.converter import convert
from app.convertor import currency_convertor, exchange_rates

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

    #requesting the amount from the currency form page
    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST":
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    base_currency = request_data.get("base_currency") or "USD"
    currency_to = request_data.get("currency_to") or "EUR"
    amount = request_data.get("amount") or 10

    # only allow floats to pass through.
    try:
        float(amount)
    except ValueError:
        print("not a float")
        flash("Currency error. Please try again", "danger")
        return redirect("/currency/form")

    results = currency_convertor(base_currency,currency_to,amount)
    exchange_rate=exchange_rates(base_currency,currency_to)
    #exchange_rate = exchange_rate(base_currency)
    print("Here are the results:", results)
    print(type(amount))

    if results:
        results = round(results,2)
        exchange_rate = round(exchange_rate,2)
        flash("Successful !", "success")
        return render_template("currency_results.html", base_currency=base_currency,currency_to=currency_to,amount=amount, results=results, exchange_rate=exchange_rate)
    else:
        flash("Currency error. Please try again", "danger")
        return redirect("/currency/form")


#https://fixer.io/symbols for currency list
