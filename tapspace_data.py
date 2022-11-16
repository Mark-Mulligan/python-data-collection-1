import httpx
import asyncio
from bs4 import BeautifulSoup


def mallet_data_query(page: int):
    return f"https://www.tapspace.com/index.php?p=catalog&parent=114&pg={page}&ajax=true&mode=catalog&selected_filters=&CatalogSetSortBy=priority&action_relaod=1"

def find_solo_page_urls(url_function):
    url_list = []
    page = 1

    while True:
        url: str = url_function(page)
        r = httpx.get(url)
        print(r.status_code)

        # end loop if page errors on request
        if r.status_code != 200:
            break

        soup = BeautifulSoup(r.text, features="html.parser")
        no_items_found_text = soup.h3

        # end loop if page request returns items not found
        if no_items_found_text and no_items_found_text.contents[0] == 'No items found':
            break

        titles = soup.findAll('div', class_="catalog-product-title")

        for title in titles:
            url_list.append(title.contents[0]['href'])

        page += 1
    
    return url_list


if __name__ == '__main__':
    url_list = find_solo_page_urls(mallet_data_query)
    print(url_list)

