from bs4 import BeautifulSoup
import requests
import json

url = "https://dolar.wilkinsonpc.com.co/divisas/dolar-diario.html"
site = requests.get(url)
soup = BeautifulSoup(site.content, 'html.parser')

elements = soup.find_all('td', class_='tabla_historico-periodos_td')
elementsList = [i.text for i in elements]

Hour = [elementsList[i] for i in range(0, len(elements), 2)]
price_string = [elementsList[i] for i in range(1, len(elements), 2)]

price_comma = [i[6:14] for i in price_string]
Price = [float(i.replace(',', "")) for i in price_comma]

data = {
    'Hour': Hour,
    'Price': Price
}

print(json.dumps(data))