import requests
from bs4 import BeautifulSoup
href = 'https://www.tiobe.com/tiobe-index/'
r = requests.get(href)
soup = BeautifulSoup(r.text, 'html.parser')
soup1 = soup.find_all('a')
print(soup1)

# print(soup.prettify())