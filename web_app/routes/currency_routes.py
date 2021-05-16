#This part is not working yet

# web_app/routes/currency_routes.py

from flask import Blueprint, request, jsonify, render_template

#from app.converter import convert
from app.converter import currency_convertor

currency_routes = Blueprint("currency_routes", __name__)

@currency_routes.route("/currency/form")
def currency_form():
    print("Currency Form...")
    return render_template("currency_form.html")


# @currency_routes.route("/currency.json")
# def currency_converter_api():
#     print("Currency Converter (API)...")
#     print("URL PARAMS:", dict(request.args))
    
#     currency_from = request.args.get("currency_from") or "USD"
#     currency_to = request.args.get("currency_to") or "EUR"
#     amount = request.args.get("amount") or "10"
#     #need some command for self 

#     #need to pass something first
#     results = currency_convertor(currency_from=currency_from, currency_to=currency_to, amount=amount)
#     if results:
#         return jsonify(results)
#     else:
#         return jsonify({"message":"Invalid input. Please try again"}), 404

