# Python program to convert the currency
# of one country to that of another country 

# Import the modules needed
import os
import json
import requests
from dotenv import load_dotenv

from app import APP_ENV

load_dotenv()

API_KEY = os.environ.get("CURRENCY_API_KEY")
url = str.__add__('http://data.fixer.io/api/latest?access_key=', API_KEY) 

response=requests.get(url)
parsed_response = response.json()
rates = parsed_response['rates']

def currency_convertor(currency_from,currency_to,amount):
    amount = float(amount)
    rate=rates[currency_from]
    amount_in_base=float(amount)/float(rate)
    result=amount_in_base*(rates[currency_to])
    return result

def exchange_rates(currency_from,currency_to):
    exchange_rate=rates[currency_to]/rates[currency_from]
    return exchange_rate


def currency_options():
    currency_list = str(rates.keys())
    return currency_list


if __name__ == "__main__":
    
    print(rates)
    # pass response variable in as parameter to the functions.
    # invoking response.json ... just pass parsed_response (not response)
    # will help with testing


    # pass in a rates 
    

#below is the example parsed response
#{"success":true,"timestamp":1621260664,"base":"EUR","date":"2021-05-17",
#"rates":{"AED":4.459446,"AFN":95.170272,"ALL":122.64449,"AMD":633.624677,"ANG":2.179655,"AOA":794.394613,"ARS":114.286026,"AUD":1.567628,"AWG":2.186504,"AZN":2.044376,"BAM":1.951923,"BBD":2.451712,"BDT":102.963935,"BGN":1.955713,"BHD":0.457651,"BIF":2398.817798,"BMD":1.21405,"BND":1.621268,"BOB":8.384485,"BRL":6.424814,"BSD":1.214279,"BTC":2.7179008e-5,"BTN":88.739492,"BWP":13.077828,"BYN":3.059376,"BYR":23795.374349,"BZD":2.447621,"CAD":1.468229,"CDF":2424.457068,"CHF":1.095218,"CLF":0.030662,"CLP":846.06835,"CNY":7.819941,"COP":4474.598741,"CRC":745.453888,"CUC":1.21405,"CUP":32.172317,"CVE":110.044712,"CZK":25.449153,"DJF":216.169053,"DKK":7.435994,"DOP":68.970503,"DZD":161.662593,"EGP":19.036539,"ERN":18.213162,"ETB":51.923387,"EUR":1,"FJD":2.461123,"FKP":0.863815,"GBP":0.861483,"GEL":4.13975,"GGP":0.863815,"GHS":7.000187,"GIP":0.863815,"GMD":62.219442,"GNF":11943.491483,"GTQ":9.365629,"GYD":253.883866,"HKD":9.429919,"HNL":29.129928,"HRK":7.5162,"HTG":108.179337,"HUF":352.463221,"IDR":17414.632577,"ILS":3.981161,"IMP":0.863815,"INR":88.986932,"IQD":1771.618162,"IRR":51117.562687,"ISK":151.100977,"JEP":0.863815,"JMD":182.51714,"JOD":0.860776,"JPY":132.611818,"KES":130.2675,"KGS":102.339537,"KHR":4932.367001,"KMF":492.721957,"KPW":1092.644883,"KRW":1380.811528,"KWD":0.365465,"KYD":1.011883,"KZT":519.340383,"LAK":11448.776108,"LBP":1831.149483,"LKR":239.211117,"LRD":208.664788,"LSL":17.142625,"LTL":3.584773,"LVL":0.734366,"LYD":5.421348,"MAD":10.724931,"MDL":21.565231,"MGA":4568.711971,"MKD":61.579987,"MMK":1891.224519,"MNT":3461.150222,"MOP":9.714254,"MRO":433.415538,"MUR":49.044737,"MVR":18.756821,"MWK":969.302631,"MXN":24.133803,"MYR":5.01499,"MZN":71.683623,"NAD":17.130928,"NGN":501.882709,"NIO":42.408456,"NOK":10.061254,"NPR":141.982948,"NZD":1.688288,"OMR":0.467404,"PAB":1.214279,"PEN":4.463202,"PGK":4.263465,"PHP":58.160279,"PKR":185.091109,"PLN":4.536345,"PYG":8119.213811,"QAR":4.420366,"RON":4.926125,"RSD":117.305178,"RUB":89.895639,"RWF":1215.896031,"SAR":4.55352,"SBD":9.69305,"SCR":19.940778,"SDG":495.331774,"SEK":10.140962,"SGD":1.622214,"SHP":0.863815,"SLL":12444.00937,"SOS":710.21895,"SRD":17.183685,"STD":25174.273204,"SVC":10.624819,"SYP":1526.71033,"SZL":17.206797,"THB":38.19643,"TJS":13.848678,"TMT":4.249174,"TND":3.310109,"TOP":2.729123,"TRY":10.13363,"TTD":8.248855,"TWD":34.123906,"TZS":2815.886294,"UAH":33.439461,"UGX":4292.442732,"USD":1.21405,"UYU":53.652041,"UZS":12829.996874,"VEF":259600519780.9039,"VND":27985.209636,"VUV":131.611749,"WST":3.054488,"XAF":654.646527,"XAG":0.04399,"XAU":0.000654,"XCD":3.28103,"XDR":0.84401,"XOF":654.646527,"XPF":119.765749,"YER":303.573378,"ZAR":17.197997,"ZMK":10927.9593,"ZMW":27.263349,"ZWL":390.924377}}

