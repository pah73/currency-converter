import os
import pytest

from app.convertor import currency_convertor, exchange_rates

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")


def test_symbol():
    invalid_results = currency_convertor(currency_from = "USD", currency_to = "FAIL", amount = 15)
    assert invalid_results == None
   # rate = "AED"
   # parsed_response = get_response(symbol)

    #assert isinstance(parsed_response, dict)
  #  assert parsed_response[]



    




# def test_hour_formatting():
#     assert format_hour("2021-03-29T21:00:00-04:00") == "21:00"
