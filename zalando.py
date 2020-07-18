import sys
import requests
from bs4 import BeautifulSoup


USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 OPR/68.0.3618.165'
LINK = 'https://www.zalando.es'
ZALANDO_LINK = 'https://www.zalando.es/catalogo/?q='

if len(sys.argv) > 1:
    for s in range(1, len(sys.argv)-1):
        sys.argv[s] = sys.argv[s] + '+'
    print('Searching...')

    final_link = ZALANDO_LINK + ''.join(sys.argv[1:])
    headers = {'user-agent': USER_AGENT}
    response = requests.get(final_link, headers = headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        results = []
        for div in soup.find_all('div', class_='cat_cardWrap-2UHT7'):
            a = div.find('a', class_='cat_imageLink-OPGGa')['href']
            link = LINK + a 
            img = div.find('img', class_='cat_image-1byrW')['src']
            title = div.find('div', class_='cat_articleName--arFp cat_ellipsis-MujnT').text

            if div.find('div', class_='cat_promotionalPrice-3GRE7'):
                price = div.find('div', class_='cat_promotionalPrice-3GRE7').text
            else:
                price = div.find('div', class_='cat_originalPrice-2Oy4G').text

            price = price.split('\xa0')[0].replace(',','.')
            item = {
                'title': title,
                'price': float(price),
                'img': img,
                'link': link
            }
            results.append(item)
            for r in range(0, len(results)):
                print(f'{results[r]} \n')

print(f'Total results: {len(results)}')