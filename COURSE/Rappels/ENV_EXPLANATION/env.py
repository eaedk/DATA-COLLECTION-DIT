import os
import requests
from typing import List, Union
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('API_KEY')
BASE_URL = os.environ.get('BASE_URL')


# to={to}&from={from}&amount={amount}
# BASE_URL= https://api.apilayer.com/currency_data/convert
# ?to=USD&from=XOF&amount=1000


def httpFetcher(URL: str,
                params=None,
                headers=None):
    with requests.Session() as session:
        result = session.get(URL,
                             params,
                             headers)
        # result = result.json()
        return result.url


def httpFetcherV2(URL: str,
                  params=None,
                  headers=None):
    result = requests.get(URL,
                          params=params,
                          headers=headers)

    result = result.json()
    return result


if __name__ == '__main__':
    result1 = httpFetcherV2(
        URL=BASE_URL,
        params={'to': 'USD',
                'from': 'XOF',
                'amount': 1000},
        headers={})

    print(result1)
    print('\n')

    # {'message': 'No API key found in request'}
    # Pour résoudre donc cette erreur
    # Mettre dans les HEADERS le API_KEY
    # {
    # 	"success":true,
    # 	"query":{
    # 	  "from":"XOF",
    # 	  "to":"USD",
    # 	  "amount":1000
    # 	},
    # 	"info":{
    # 	  "timestamp":1658516764,
    # 	  "quote":0.00155
    # 	},
    # 	"result":1.55
    # }

    result2 = httpFetcherV2(
        URL=BASE_URL,
        params={'to': 'USD',
                'from': 'XOF',
                'amount': 1000},
        headers={'apikey': API_KEY})

    print(result2)
