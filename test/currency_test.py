import os
import pytest

from app.convertor import currency_convertor, exchange_rates, currency_options

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")

#testing that the result will be zero if the amount is zero. Rates get updated every day so we wanted something that would work consistently.
def test_constant_amount():
    results = currency_convertor(currency_from = "USD", currency_to = "USD", amount = 1)
    assert results == 1.0

#testing that nothing gets returned if the currency is invalid
def test_currency_to_input():
  results = currency_convertor(currency_from = "USD", currency_to = "1345", amount = 10)
  assert results == None

def test_currency_from_input():
  results = currency_convertor(currency_from = "235", currency_to = "EUR", amount = 10)
  assert results == None


def constant_exchange_rate_test():
  results = exchange_rates(currency_from = "USD", currency_to = "USD")
  assert results == 1

#testing