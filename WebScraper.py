from urllib.request import urlopen, urlparse, urljoin
import requests
from bs4 import BeautifulSoup
import json

html = urlopen('https://www.cfcunderwriting.com/en-gb/')


bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('div',class_='img')
scripts = bs.find_all('script')

items = []
for image in images: 
    record = {"Image":image}
    items.append(str(record))

items1 = []
for script in scripts: 
    record = {"Script":script}
    items.append(str(record))

a = "https://"
for item in items:
    if a in item:
        continue
    else:
        items.remove(item)

with open('results.json', 'w', encoding='utf-8') as write_file:
 output = json.dumps(items, indent=0)
 write_file.write(output)
    