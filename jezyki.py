import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

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
        # print(a)
        d = a.find_all('td')
        nazwa = str(d[4].text)
        # nazwa1 = nazwa.replace('/','_')
        procent = str(d[5].text)
        obrazek = d[3].find('img')['src']
        # print(obrazek)
        b = a.find('td')
        c = a.find('img')
        # nazwa = c.get('alt')
        # print(b.get('td'))
        lista.write('\n')
        lista.write(str(l) + '.\n')
        lista.write('![](https://www.tiobe.com')
        lista.write(obrazek + ')' + '\n')
        lista.write('[')
        lista.write(nazwa)
        lista.write('](../')
        lista.write(nazwa)
        lista.write(')\n')
        lista.write(procent)
        lista.write('\n')
        with open(f'{nazwa}.md', 'w') as jezyk:
            jezyk.write('kotki na niebie')
            # results = DDGS().answers(nazwa1)
            # print(str(results))
            # jezyk.write(str(results))
        l = l + 1
        print('\n')
