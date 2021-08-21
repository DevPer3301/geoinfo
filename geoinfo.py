import requests
import doctest
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
    """
    Getting capital of the country


    >>> print(get_capital("Ukraine"))
    Kiev

    >>> print(get_capital("Canada"))
    Ottawa

    >>> print(get_capital("Australia"))
    Canberra
    """
    data_info = get_info(country)
    try:
        return data_info[0]["capital"]
    except (KeyError, ValueError):
        raise UnknownCountry(country) from  None

def get_region(country):
    """
    Getting the region of the country


    >>> print(get_region("Australia"))
    Oceania

    >>> print(get_region("China"))
    Asia

    >>> print(get_region("Germany"))
    Europe
    """
    data_info = get_info(country)
    try:
        return data_info[0]["region"]
    except (KeyError, ValueError):
        raise UnknownCountry(country) from None


def get_population(country):
    """
    Getting population of the country


    >>> print(get_population("China"))
    1377422166

    >>> print(get_population("Russia"))
    146599183

    >>> print(get_population("USA"))
    323947000
    """
    data_info = get_info(country)
    try:
        return data_info[0]["population"]
    except (KeyError, ValueError):
        raise UnknownCountry(country) from None


def get_area(country):
    """
    Getting area of the country


    >>> print(get_area("Canada"))
    9984670.0

    >>> print(get_area("Russia"))
    17124442.0

    >>> print(get_area("Saudi Arabia"))
    2149690.0
    """
    data_info = get_info(country)
    try:
        return data_info[0]["area"]
    except (KeyError, ValueError):
        raise UnknownCountry(country) from None


def get_currency(country):
    """Getting currency of the country


    >>> print(get_currency("China"))
    {'code': 'CNY', 'name': 'Chinese yuan', 'symbol': '¥'}

    >>> print(get_currency("Qatar"))
    {'code': 'QAR', 'name': 'Qatari riyal', 'symbol': 'ر.ق'}

    >>> print(get_currency("Japan"))
    {'code': 'JPY', 'name': 'Japanese yen', 'symbol': '¥'}
    """
    data_info = get_info(country)
    try:
        currency_info = data_info[0]["currencies"][0]
        return currency_info
    except (KeyError, ValueError):
        raise UnknownCountry(country) from None

def get_borders(country):
    """
    Getting borders of the country


    >>> print(get_borders("Thailand"))
    ['MMR', 'KHM', 'LAO', 'MYS']

    >>> print(get_borders("Qatar"))
    ['SAU']

    >>> print(get_borders("Australia"))
    []
    """
    data_info = get_info(country)
    try:
        return data_info[0]["borders"]
    except (KeyError, ValueError):
        raise UnknownCountry(country) from None
doctest.testmod()


