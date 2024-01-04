import requests
from django.conf import settings


URL = "https://api.apilayer.com/exchangerates_data/latest"
PARAMS = {
  'base': 'RUB'
}
HEADERS = {
  "apikey": settings.EXCHANGE_RATE_API_KEY
}


def get_exchange_rate(currency):
    """
    Возвращает словарь с данными о курсе
    :param currency: валюта
    :return: курс (float)
    """
    currency = currency.upper()

    response = requests.request("GET", URL, headers=HEADERS, params=PARAMS)
    status_code = response.status_code

    if status_code == 200:
        result = response.json()

        if result['rates'].get(currency) is not None:
            return result['rates'][currency]

    result = 1

    return result
