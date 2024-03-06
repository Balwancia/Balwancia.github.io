import requests
from bs4 import BeautifulSoup
href = 'https://www.tiobe.com/tiobe-index/'
r = requests.get(href).content

soup = BeautifulSoup(r, 'html.parser')
tab = soup.find('table').find('tbody').find_all('tr')

with open(f'jezyki_programowania.md', 'w') as lista:
    lista.write("20 najpopularniejszych języków programowania:")
    lista.write('\n')
    l = 1
    for i in tab:
        a = i
        print(a)
        with open(f'{l}.md', 'w') as jezyk:
            jezyk.write("balwanki są super")
            l = l + 1
        b = a.find('td')
        c = a.find('img')
        nazwa = c.get('alt')
        # print(b.get('td'))
        lista.write('\n')
        # lista.write(str(b))
        # print(a.find('td'))
        # print(a.find('img'))
        # print(c.h)
        lista.write('[')
        lista.write(str(nazwa))
        lista.write('](../')
        lista.write(str(l))
        lista.write(')')
        lista.write('\n')
        # lista.write(str(c))
        # print(tab.find'tr'))
        print('\n')
# print(tab)


# print(soup.prettify())