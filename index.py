import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.tapspace.com/marimba-xylophone/')
soup = BeautifulSoup(r.text, features="html.parser")
cards = soup.findAll('div', class_='catalog-list2')

# https://www.tapspace.com/index.php?p=catalog&parent=114&pg=5&ajax=true&mode=catalog&selected_filters=&CatalogSetSortBy=priority&action_relaod=1

solo_data = []

for card in cards:
    title_info = card.find('div', class_="catalog-product-title")
    data = { 'title': title_info.a.contents[0] }
    solo_data.append(data)
	  
print(solo_data)
  