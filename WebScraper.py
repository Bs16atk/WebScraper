from urllib.request import urlopen, urlparse, urljoin
import requests
from bs4 import BeautifulSoup
import json

html = urlopen('https://www.cfcunderwriting.com/en-gb/')


bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('div',class_='img')
scripts = bs.find_all('script')
links = bs.find_all('link')
morelinks = bs.find_all('a', href=True)

items = []
for image in images: 
    record = {"Image":image}
    items.append(str(record))

for script in scripts: 
    record = {"Script":script}
    items.append(str(record))

for link in links: 
    record = {"Link":link}
    items.append(str(record))

a = 'https://'
for item in items:
    if a in item:
        continue
    else:
        items.remove(item)

with open('results.json', 'w', encoding='utf-8') as write_file:
 output = json.dumps(items, indent=2)
 write_file.write(output)

#Task 2
for x in morelinks:
    if "privacy" in str(x):
        print("The Privacy Policy can be found at: " + str(x))
    
    