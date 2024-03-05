import requests
from bs4 import BeautifulSoup
href = 'https://www.tiobe.com/tiobe-index/'
r = requests.get(href)
print('--- # AWWW ---')
print('--- Anna Piórkowska ---')
print('--- [20 najlpopularnijeszych jezyków programowania](balwancia.github.io/jezyki-programowania) ---')
# prsint(r.text)

# soup = BeautifulSoup(r.text, 'html.parser')
# soup1 = soup.find_all('table')
# print(soup1)

# print(soup.prettify())