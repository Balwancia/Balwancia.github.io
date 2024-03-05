import requests
from bs4 import BeautifulSoup
href = 'https://www.tiobe.com/tiobe-index/'
r = requests.get(href)
print('permalink: [20 najpopularniejszych jezyków programowania](../jezyki_programowania)')
# prsint(r.text)

# soup = BeautifulSoup(r.text, 'html.parser')
# soup1 = soup.find_all('table')
# print(soup1)

# print(soup.prettify())