import sys
from bs4 import BeautifulSoup
import requests
from operator import attrgetter

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 OPR/68.0.3618.165'
DEFSHOP_LINK = 'https://en.def-shop.com/index.php?rf=2&search='
ASOS_LINK = 'https://www.asos.com/search/?q='
END_LINK = 'https://www.endclothing.com/en-de/catalogsearch/results?q='

class Product:
    def __init__(self, name, price, link, image, shop):
        self.name = name
        self.price = price
        self.link = link
        self.image = image 
        self.shop = shop
    def __str__(self):
        return f"Product Name:{self.name}, price: {self.price}"
    def __repr__(self):
        return repr((self.name, self.price))

if len(sys.argv) > 1:
    for s in range(1, len(sys.argv)-1):
        sys.argv[s] = sys.argv[s] + '+'
    print('Searching...')

    link_asos = ASOS_LINK + ''.join(sys.argv[1:])
    link_end = END_LINK + ''.join(sys.argv[1:])
    link_def = DEFSHOP_LINK + ''.join(sys.argv[1:])
    headers = {"user-agent" : USER_AGENT}
    res_asos = requests.get(link_asos, headers = headers)
    res_def = requests.get(link_def, headers = headers)
    res_end = requests.get(link_end, headers = headers)
    