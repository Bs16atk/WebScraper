from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import json

html = urlopen('https://www.cfcunderwriting.com/en-gb/')


bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img')
fonts = bs.find_all('link')

items = []
for image in images: 
    record = {"Image":image}
    items.append(str(record))
    print(record)
#print(items)

items1 = []
for font in fonts: 
    record1 = {"Font":font}
    items1.append(str(record1))
    print(record1)
#print(items)

items.append(items1)

with open('results.json', 'w', encoding='utf-8') as write_file:
 output = json.dumps(items, indent=2)
 write_file.write(output)
    