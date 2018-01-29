from bs4 import BeautifulSoup
from avito_req import get_html

html = get_html('https://www.avito.ru/pervouralsk')

bs = BeautifulSoup(html, 'html.parser')

avito_sale = {}

for advertisement in bs.find_all('div', class_='item_table'):
	title = advertisement.find('a', class_='item-description-title-link')
	price = advertisement.find('div', class_='about').contents[0]
	avito_sale['title'] = title.get('title')
	avito_sale['price'] = price.strip()
	avito_search = []
	avito_search.append(avito_sale)
	print(avito_search)