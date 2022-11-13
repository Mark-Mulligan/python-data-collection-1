import requests
from bs4 import BeautifulSoup


def get_title_and_composer(card):
    title_info = card.find('div', class_='catalog-product-title')
    composer_info = title_info.find('a', class_='catalog-mfr-name')
    title = title_info.a.contents[0]
    composer = composer_info.contents[0]
    return {'title': title, 'composer': composer}

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
        title_data = get_title_and_composer(card)
        mallet_solo_data.append({"title": title_data['title'], "composer": title_data['composer']})

    page += 1

print(mallet_solo_data)
print(len(mallet_solo_data))

