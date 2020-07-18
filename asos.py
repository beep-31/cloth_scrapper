import bs4
import requests
import sys
from operator import itemgetter, attrgetter, methodcaller

class Product:
    def __init__(self, title, price, link, img):
        self.title = title
        price = price.split('£')
        self.price = float(price[1])
        self.link = link
        self.img = img
    def __str__(self):
        return f"Product Name:{self.title}, price: {self.price} \n Product link: {self.link} \n Product image: {self.img}"
    def __repr__(self):
        return repr((self.title, self.price))

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 OPR/68.0.3618.165'
ASOS_LINK = 'https://www.asos.com/es/search/?q='

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)-1):
        sys.argv[i] = sys.argv[i] + '+'
    print('Searching...')
    final_link = ASOS_LINK + ''.join(sys.argv[1:])
    headers = {"user-agent":USER_AGENT}
    res = requests.get(final_link, headers = headers)

    if res.status_code == 200:
        soup = bs4.BeautifulSoup(res.content, 'html.parser')
        results = []
        for a in soup.find_all('article', class_='_2qG85dG'):
            anchor = a.find('a', class_='_3TqU78D')
            if anchor:
                print(f'{anchor} \n')
                title = anchor.text
                split_title = title.split('£')
                final_title = split_title[0]
                link = anchor['href']
                img = a.find('img').get('src')
                # img = anchor.find('img')
            paragraphs = soup.find_all('p', class_='_1ldzWib')
            if paragraphs:
                if a.find('span', class_='_16nzq18'):
                    price = a.find('span', class_='_16nzq18').text
                else:
                    price = a.find('span', class_='_3VjzNxC').text
            item = Product(final_title, price, link, img)
            results.append(item)
        
    result_sorted = sorted(results, key=attrgetter('price'), reverse=False)
    for i in range(0, len(result_sorted)):
        print(f'{i+1}){result_sorted[i]}\n')
    print(f'Total results: {len(results)}')
