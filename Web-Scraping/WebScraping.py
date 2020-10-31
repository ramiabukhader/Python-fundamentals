# we want to scrape the content of the demo file i've created to make a better understanding of the webscaraping
from bs4 import BeautifulSoup

raw_html = open('demo.html').read()

# html = BeautifulSoup(raw_html, 'html.parser') #read about parser for better understanding

# for p in html.select('p'): # selected the paragraph tag
#     print(p)