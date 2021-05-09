#This part is not working yet

# web_app/routes/currency_routes.py

from flask import Blueprint, request, jsonify

from app.converter import convert

currency_routes = Blueprint("currency_routes", __name__)

@currency_routes.route("/currency.json")
def currency_converter_api():
    print("Currency Converter (API)...")
    print("URL PARAMS:", dict(request.args))

    from_currency = request.args.get("from_currency") or "USD"
    to_currency = request.args.get("to_currency") or "EUR"
    amount = request.args.get("amount") or "10"

    results = convert(from_currency=from_currency, to_currency=to_currency, amount=amount)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message":"Invalid input. Please try again"}), 404

