import requests
from bs4 import BeautifulSoup

datos = requests.get('https://www.eurogamer.es/articles/2016-08-04-pokemon-go-tabla-de-tipos-puntos-fuertes-y-debiles-de-cada-uno')
soup = BeautifulSoup(datos.text, 'html.parser')

tablaTipos = soup.find('table', class_ = '')
print('|{:^15s} |{:^50s} |{:^55s} |{:^70s} |{:^50s}|'.format('Tipo','Fuerte contra','Debil contra','Resistente a','Vulnerable a'))
print()
for tipo in tablaTipos.find_all('tbody'):
    rows = tipo.find_all('tr')
    for row in rows:
        Ctipo = row.find('td', class_ ='').text.strip()
        CFuerte = row.find_all('td', class_ = '')[1].text
        CDebil  = row.find_all('td', class_ = '')[2].text
        CResistente= row.find_all('td', class_ = '')[3].text
        CVulnerable= row.find_all('td', class_ = '')[4].text
        print('|{:^15s} |{:^50s} |{:^55s} |{:^70s} |{:^50s}|'.format(Ctipo,CFuerte,CDebil,CResistente,CVulnerable))