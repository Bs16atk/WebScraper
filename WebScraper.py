#importing a load of libraries
from urllib.request import urlopen, urlparse, urljoin
import re
import requests
from collections import Counter
from string import punctuation
from bs4 import BeautifulSoup
import json
#Task1
print("Scraping Index Page")
html = urlopen('https://www.cfcunderwriting.com/en-gb/')

#Scrape the index page
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('div',class_='img')
scripts = bs.find_all('script')
links = bs.find_all('link')
morelinks = bs.find_all('a', href=True)

#Task2

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

#Trying to only show external resources, this mostly worked
a = 'https://'
for item in items:
    if a in item:
        continue
    else:
        items.remove(item)

#Writing results to rescources.json
with open('resources.json', 'w', encoding='utf-8') as write_file:
 output = json.dumps(items, indent=2)
 write_file.write(output)
 print("\nWrote to resources.json")


#Task 3 to find the privacy policy by enumerating through the links in the page

for x in morelinks:
    if "privacy" in str(x):
        privlink = str(x)
        print("\nThe Privacy Policy can be found at: " + str(x))

  
#Task 4 to scrape the privacy policy page and perform a word frequency count

print("\nScraping Privacy Policy")
r = requests.get("https://www.cfcunderwriting.com/en-gb/support/privacy-policy/")
bs1 = BeautifulSoup(r.content, 'html.parser')

#getting text from paragraphs
text_p = (''.join(bs1.findAll(text=True))for thing in bs1.findAll('p'))
c_p = Counter((x.rstrip(punctuation).lower() for y in text_p for x in y.split()))

#getting text from divs
text_div = (''.join(bs1.findAll(text=True))for thing in bs1.findAll('div'))
c_div = Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))

total = c_div + c_p
list_most_common_words = total.most_common()
words = total.most_common(1000)
#reformatting the word frequency count to what I think is more like JSON
words1 = json.dumps(dict(words), indent=2)

#writing the new results to wordfrequencycount.json
with open('wordfrequencycount.json', 'w', encoding='utf-8') as write_file:
 output = json.dumps(items, indent=2)
 write_file.write(words1)

print("\nWrote to wordfrequencycount.json")