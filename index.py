import requests
from bs4 import BeautifulSoup
import pprint
import re

pp = pprint.PrettyPrinter(indent=4)

# 4 Mallet query
# https://www.tapspace.com/index.php?p=catalog&parent=114&pg=2&ajax=true&mode=catalog&selected_filters=,filter_333_42&CatalogSetSortBy=priority&action_relaod=1


def four_mallet_data_query(page: int):
    return f"https://www.tapspace.com/index.php?p=catalog&parent=114&pg={page}&ajax=true&mode=catalog&selected_filters=,filter_333_42&CatalogSetSortBy=priority&action_relaod=1"


def two_mallet_data_query(page: int):
    return f"https://www.tapspace.com/index.php?p=catalog&parent=114&pg={page}&ajax=true&mode=catalog&selected_filters=,filter_334_42&CatalogSetSortBy=priority&apply_filters=yes&container=filters"


def get_title_and_composer(card):
    title_info = card.find('div', class_='catalog-product-title')
    composer_info = title_info.find('a', class_='catalog-mfr-name')
    title = title_info.a.contents[0]
    composer = composer_info.contents[0]
    return {'title': title, 'composer': composer}

def get_description(card):
    description_info = card.find('div', class_='catalog-overview')
    description = description_info.contents[0]
    return description

def get_duration(card):
    solo_info = card.find('div', class_='catalog-fields').contents
    duration = ''
    
    for index, item in enumerate(solo_info):
        match = re.search('duration', str(item), re.IGNORECASE)  # type: ignore
        if match:
            duration = solo_info[index + 1]
        

    return duration



def parse_mallet_solos_data(data_list: list, url_function, sub_category: str):
    page = 1

    while True:
        url: str = url_function(page)
        r = requests.get(url)

        print(r.status_code)

        # end loop if page errors on request
        if r.status_code != 200:
            break

        soup = BeautifulSoup(r.text, features="html.parser")
        no_items_found_text = soup.h3

        # end loop if page request returns items not found
        if no_items_found_text and no_items_found_text.contents[0] == 'No items found':
            break

        cards = soup.findAll('div', class_="catalog-list2")

        for card in cards:
            title_data = get_title_and_composer(card)
            description_data = get_description(card)
            duration = get_duration(card)
            print(duration)
            # pp.pprint(duration)
            data_list.append(
            {"title": title_data['title'], "composer": title_data['composer'], 'sub_category': sub_category, 'description': description_data})

        page += 1
    
    return data_list

if __name__ == '__main__':
    mallet_solo_data = [] 
    # parse_mallet_solos_data(mallet_solo_data, four_mallet_data_query, 'four_mallets')
    parse_mallet_solos_data(mallet_solo_data, two_mallet_data_query, 'two_mallets')

    # pp.pprint(mallet_solo_data)
    # print(len(mallet_solo_data))
