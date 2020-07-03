import sys
import requests
from bs4 import BeautifulSoup

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 OPR/68.0.3618.165'
SNEAKER_PAGE = 'https://www.sneakersnstuff.com/en/search/searchbytext?key='

if len(sys.argv) > 1:
    for s in range(1, len(sys.argv)-1):
        sys.argv[s] = sys.argv[s] + '+'
    print('Searching...')
    final_link = SNEAKER_PAGE + ''.join(sys.argv[1:])
    print(final_link)
    headers = {"user-agent": USER_AGENT}
    response = requests.get(final_link, headers = headers)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        results = []
        for div in soup.find_all('div', class_='card__content'):
            link = div.find('a', class_='card__link')['href']
            title = div.find('strong', class_='card__name').text
            price = div.find('span', class_='price__current').text
            img = div.find('img', class_='card-img card-img embed-responsive-item ls-is-cached lazyloaded')['src']
            item = {
                'title': title,
                'price': price,
                'link': link,
                'img': img
            }

            results.append(item)
            for r in range(0, len(results)):
                print(f'{results[r]} \n')

