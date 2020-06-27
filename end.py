import sys
import requests
import bs4 as bs

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 OPR/68.0.3618.165'
END_LINK = 'https://www.endclothing.com/en-de/catalogsearch/results?q='

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)-1):
        sys.argv[i] = sys.argv[i] + '+'
    print('Searching...')
    final_link = END_LINK + ''.join(sys.argv[1:])
    headers = {"user-agent":USER_AGENT}
    req = requests.get(final_link, headers = headers)

    if req.status_code == 200:
        soup = bs.BeautifulSoup(req.content, 'html.parser')
        results = []
        for a in soup.find_all('a', class_='sc-1koxpgo-0 bTJixI sc-5sgtnq-2 gHSLMJ'):
            title = a.find('span', class_='sc-5sgtnq-3 dMAnEc').text
            div = a.find('div', class_='sc-5sgtnq-5 kyzPqp')
            if div:
                price = div.find('span').text
                price = price.split('€')
                final_price = int(price[1])
                item = {
                    'title':title,
                    'price':final_price
                }
            else:
                div = a.find('div', class_='sc-5sgtnq-5 oqeJw')
                price = div.find_all('span')
                print(len(price))
                if len(price) > 1:
                    price = div.select('span')[1].get_text(strip = True)
                    price = price.split('€')
                    final_price = int(price[1])
                else:
                    final_price = price
                item = {
                    'title':title,
                    'price':final_price
                }

            results.append(item)
        if len(results) > 0:
            for r in range(0, len(results)):
                print(f'{results[r]} \n')
            print(f'Total results:{len(results)}')
        else:
            print('No items were found')
            
