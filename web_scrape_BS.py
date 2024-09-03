# simple web scraping using Beautiful Soup.
# https://beautiful-soup-4.readthedocs.io/en/latest/

import requests
from bs4 import BeautifulSoup

url = 'https://www.rd.com/list/common-cat-myths'

# adding user-agent to mimic sending request from a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
except Exception as e:
    raise SystemExit(e)

soup = BeautifulSoup(response.text, 'html.parser')

for img in soup.find_all('img'):
    if '.jpg' in img['src'] and 'cat' in img['src']:
        # just print the link for now. we can also save it to disk if needed
        print(img['src'])
