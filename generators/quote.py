import requests


class Generate:
    @staticmethod
    def quote():
        url = 'http://api.forismatic.com/api/1.0/'
        params = {
            'method': 'getQuote',
            'format': 'json',
            'key': '6',
            'lang': 'ru',

        }
        response = requests.post(url, params=params)
        return response.json()['quoteText']

