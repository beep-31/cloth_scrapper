import bs4
import requests
import sys

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 OPR/68.0.3618.165'
DEFSHOP_LINK = 'https://en.def-shop.com/index.php?rf=2&search={}'

if len(sys.argv) > 1:
    for s in range(1, len(sys.argv)-1):
        sys.argv[s] = sys.argv[s] + '+'
    print('Searching...')
    final_link = DEFSHOP_LINK + ''.join(sys.argv[1:])
    headers = {'user_agent': USER_AGENT}

    request = requests.get(final_link, headers = headers)
    if request.status_code == 200:
        soup = bs4.BeautifulSoup(request.content, 'html5lib')
        results = []
        for i in soup.find_all('div', class_ = 'product-info'):
            price = i.find('div', class_='product-price').text
            if price:
                final_price = price.split('£ ')
            title = i.find('div', class_='product-cat').text
            img = i.find('img').get('data-retina')
            img = str(img)
            img = img.split('f=auto/')
            print(img)
            item = {
                'title': title,
                'price': float(final_price[-1].replace(',','.')),
                'img': img[-1]
            }
            results.append(item)

        for r in range(0, len(results)):
            print(f'{results[r]} \n')

else:
    print('Write an item you are looking for')
