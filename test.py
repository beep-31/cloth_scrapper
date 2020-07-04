string = '104,95\xa0€'
print(string.split('\xa0')[0].replace(',', '.'))