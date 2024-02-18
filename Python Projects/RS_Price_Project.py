import requests
from bs4 import BeautifulSoup

def scrape_runescape3_items(url):
    items = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        item_divs = soup.find_all('div', class_='col-2 float-left cards p-2')
        for div in item_divs:
            # Extract item name
            item_name_element = div.find('h4', class_='text-white font-weight-bold')
            if item_name_element:
                item_name = item_name_element.text.strip()
                # Check if item name contains "OSRS"
                if 'OSRS' not in item_name:
                    items.append(item_name)
                else:
                    print('Filtered out OSRS item:', item_name)
            else:
                print('Item name not found in a div')
        return items
    else:
        print('Failed to fetch webpage:', response.status_code)
        return None

# URL of the page containing RS3 items
url = 'https://www.ely.gg/items'

# Scrape the RS3 item names
rs3_items = scrape_runescape3_items(url)

# Print the scraped item names
if rs3_items:
    for item in rs3_items:
        print('Item:', item)
