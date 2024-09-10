# api docs: https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide


import requests

# INSERT API KEY HERE
API_KEY = ''

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}


# Using CoinMarketCap IDs is always recommended as not all cryptocurrency symbols are unique. They can also change with a cryptocurrency rebrand.
def get_currency_id(symbol):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

    params = {
        'symbol': symbol,
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
    except Exception as err:
        raise SystemExit(err)

    return response.json().get('data')[0].get('id')


def get_currency_price(id):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

    params = {
        'id': str(id),
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
    except Exception as err:
        raise SystemExit(err)

    return response.json()\
        .get('data')\
        .get(str(id))\
        .get('quote')\
        .get('USD')\
        .get('price')


if __name__ == '__main__':
    from pprint import pprint
    id = get_currency_id('BTC')
    print(get_currency_price(id))
