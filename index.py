import requests
from bs4 import BeautifulSoup


def get_title(card):
    title_info = card.find('div', class_='catalog-product-title')
    return title_info.a.contents[0]

page = 1
mallet_solo_data = []

while True:
    r = requests.get(
        f"https://www.tapspace.com/index.php?p=catalog&parent=114&pg={page}&ajax=true&mode=catalog&selected_filters=&CatalogSetSortBy=priority&action_relaod=1'")

    if r.status_code != 200:
        break

    soup = BeautifulSoup(r.text, features="html.parser")
    cards = soup.findAll('div', class_="catalog-list2")

    for card in cards:
        title = get_title(card)
        mallet_solo_data.append({"title": title})

    page += 1

print(mallet_solo_data)
print(len(mallet_solo_data))

