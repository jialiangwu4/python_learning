# This program will make an API call to the useless facts website and print a random fact to the console.

import requests

url = 'https://uselessfacts.jsph.pl/random.json'

params = {
    'language': 'en'
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
except Exception as e:
    raise SystemExit(e)

print(response.json().get('text'))
