import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

href = 'https://www.tiobe.com/tiobe-index/'
r = requests.get(href).content

soup = BeautifulSoup(r, 'html.parser')
tab = soup.find('table').find('tbody').find_all('tr')

with open(f'index.md', 'w') as index:
    index.write('# Witaj na mojej stronie, dla takiej osoby jak Ty, to warto się roztopić!\n' + 
                '[20 najpopularniejszych jezyków programowania](../jezyki_programowania)' +
                '![](https://images.emojiterra.com/google/android-12l/512px/2603.png)') 

with open(f'jezyki_programowania.md', 'w') as lista:
    lista.write("# 20 najpopularniejszych języków programowania:")
    lista.write('\n')
    l = 1
    for i in tab:
        a = i
        d = a.find_all('td')
        nazwa = str(d[4].text)
        nazwa1 = nazwa.replace('/','_')
        procent = str(d[5].text)
        obrazek = d[3].find('img')['src']
        b = a.find('td')
        c = a.find('img')
        lista.write('\n' + str(l) + '.\n')
        lista.write('![](https://www.tiobe.com' + obrazek + ')' + '\n')
        lista.write('[' + nazwa1 + '](../' + nazwa1 + ')\n')
        lista.write(procent + '\n')
        with open(f'{nazwa1}.md', 'w') as jezyk:
            results = DDGS().text(nazwa1 + 'język programowania', region='pl-pl', max_results=1)
            t = results[0]['body']
            jezyk.write('# ' + nazwa + '\n')
            jezyk.write(t + '\n')
            jezyk.write('Źródło: ')
            h = results[0]['href']
            jezyk.write(h)
        l = l + 1
