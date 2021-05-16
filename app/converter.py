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
    rate=response.json()['rates'][currency_from]
    amount_in_base=amount/rate
    result=amount_in_base*(response.json()['rates'][currency_to])
    print(amount_in_base)
    print(type(amount_in_base))
    print(type(rate))
    print(type(result))
    print(rate)
    print(result)


response=requests.get(url)
base_currency=input('Enter the base currency:')
convert_to=input('Enter the result currency:')
# base_currency=input('Enter the base currency from '+str(response.json()['rates'].keys()))
# convert_to=input('Enter the result currency '+str(response.json()['rates'].keys()))
amount_to_convert=int(input("Enter the amount to convert"))
currency_convertor(base_currency,convert_to,amount_to_convert)






# source for code below: https://www.geeksforgeeks.org/currency-converter-in-python/

# class Currency_convertor:
#     # empty dict to store the conversion rates
#     rates = {} 
#     def __init__(self, url):
#         data = requests.get(url).json()
  
#         # Extracting only the rates from the json data
#         self.rates = data["rates"] 
  
#     # function to do a simple cross multiplication between 
#     # the amount and the conversion rates
#     def convert(self, from_currency, to_currency, amount):
#         initial_amount = amount
#         if from_currency != 'EUR' :
#             amount = amount / self.rates[from_currency]
  
#         # limiting the precision to 2 decimal places
#         amount = round(amount * self.rates[to_currency], 2)
#         print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
  
# # Driver code
# if __name__ == "__main__":
  
#     CURRENCY_API_KEY = "ed8098eb0481545d8a4822cdd2b09f08"
#     url = str.__add__('http://data.fixer.io/api/latest?access_key=', CURRENCY_API_KEY) 
#     c = Currency_convertor(url)
#     from_country = input("From Country: ")
#     to_country = input("TO Country: ")
#     amount = int(input("Amount: "))
  
#     c.convert(from_country, to_country, amount)
