import requests
from functools import lru_cache
class UnknownCountry(Exception):
    def __init__(self,country):
        self.country = country
    def __str__(self):
        return "{} is unknown".format(self.country)
@lru_cache(None)
def get_info(country):
    url = "https://restcountries.eu/rest/v2/name/{}".format(country.lower())
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
    data_info = requests.get(url, headers).json()
    return data_info


def get_capital(country):
    data_info = get_info(country)
    try:
        return data_info[0]["capital"]
    except (KeyError, ValueError):
        raise UnknownCountry(country) from  None

def get_region(country):
    data_info = get_info(country)
    try:
        return data_info[0]["region"]
    except (KeyError, ValueError):
        raise UnknownCountry(country) from None


def get_population(country):
    data_info = get_info(country)
    try:
        return data_info[0]["population"]
    except (KeyError, ValueError):
        raise UnknownCountry(country) from None


def get_area(country):
    data_info = get_info(country)
    try:
        return data_info[0]["area"]
    except (KeyError, ValueError):
        raise UnknownCountry(country) from None


def get_currency(country):
    data_info = get_info(country)
    try:
        currency_info = data_info[0]["currencies"][0]
        return currency_info
    except (KeyError, ValueError):
        raise UnknownCountry(country) from None

def get_borders(country):
    data_info = get_info(country)
    try:
        return data_info[0]["borders"]
    except (KeyError, ValueError):
        raise UnknownCountry(country) from None