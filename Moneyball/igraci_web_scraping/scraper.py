import requests
from bs4 import BeautifulSoup    # PyPI name: beautifulsoup4
import pandas as pd
import csv
url = 'https://www.whoscored.com/Statistics'

r = requests.get(url)
data = r.text
with open('html_kod.html', 'w', encoding='utf-8') as f:
    f.write(data)

with open('html_kod.html', 'r', encoding='utf-8') as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')
table = soup.find('table')
print(table)
#cells= table.find_all('td')

