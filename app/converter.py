# Python program to convert the currency
# of one country to that of another country 

# Import the modules needed
import os
import json
import requests
from dotenv import load_dotenv

#from app import APP_ENV

#NOTE - This needs to eventually be passed through __init__.py. put it here so it can work while i'm testing
APP_ENV = os.getenv("APP_ENV", default="production")

load_dotenv()

CURRENCY_API_KEY = "ed8098eb0481545d8a4822cdd2b09f08"
url = str.__add__('http://data.fixer.io/api/latest?access_key=', CURRENCY_API_KEY) 


def currency_convertor(currency_from,currency_to,amount):
    amount = float(amount)
    rate=response.json()['rates'][currency_from]
    amount_in_base=float(amount)/float(rate)
    result=amount_in_base*(response.json()['rates'][currency_to])
    return result

def exchange_rates(currency_from,currency_to):
    exchange_rate=(response.json()['rates'][currency_to])/(response.json()['rates'][currency_from])
    return exchange_rate


def currency_options():
    currency_list = str(response.json()['rates'].keys())
    return currency_list



response=requests.get(url)

