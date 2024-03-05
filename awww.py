import requests
from bs4 import BeautifulSoup
href = 'https://www.tiobe.com/tiobe-index/'
r = requests.get(href)
print('--- [20 najpopularniejszych jezyków programowania](balwancia.github.io/strona/jezyki-programowania) ---')
# prsint(r.text)

# soup = BeautifulSoup(r.text, 'html.parser')
# soup1 = soup.find_all('table')
# print(soup1)

# print(soup.prettify())