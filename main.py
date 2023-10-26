import requests
from bs4 import BeautifulSoup

game_titiles = []
game_prices = []
game_discounts = []

for i in range(1, 2):
    response = requests.get(
        'https://store.steampowered.com/search/?sort_by=&sort_order=0&page=' + str(i))
    soup = BeautifulSoup(response.text, 'html.parser')

    steam_name_tags = soup.find_all('span', class_='title')
    steam_price_tags = soup.find_all('div', class_='discount_final_price')
    steam_discount_tags = soup.find_all('div', class_='discount_pct')
    
    for name_tag in steam_name_tags:
        game_titiles.append(name_tag.text)

    for steam_price_tag in steam_price_tags:
        game_prices.append(steam_price_tag.text)

    for steam_discount_tag in steam_discount_tags:
        game_discounts.append(steam_discount_tag.text)


print(game_titiles)
print(game_prices)
print(game_discounts)
