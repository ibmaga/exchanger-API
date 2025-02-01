from requests import get
from app.errors.handlers import CurrencyError

url = 'https://api.apilayer.com/currency_data'
header = {'apikey': 'r58kJ3bwsLtbLOr66sQ6blNILH7zfprh'}
lst = '/list'
live = '/live'
conv = '/convert'


class REQ:
    @classmethod
    def get_fresh_currency(cls, source: str):
        data = {'source': source.upper()}
        response = get(url + live, headers=header, params=data)
        jsn = response.json()
        if jsn['success']:
            return jsn['quotes']

        raise CurrencyError()

    @classmethod
    def get_currency_list(cls):
        response = get(url + lst, headers=header)
        jsn = response.json()
        if jsn['success']:
            return jsn['currencies']

        raise CurrencyError()
