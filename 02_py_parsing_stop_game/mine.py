
import requests
import bs4

response = requests.get('https://stopgame.ru/solutions/p5')
soup = bs4.BeautifulSoup(response.text, 'html.parser')

games = soup.find("div", class_="_default-grid_1cdv7_258")
#w0 > div._default-grid_1cdv7_258

print(games)
