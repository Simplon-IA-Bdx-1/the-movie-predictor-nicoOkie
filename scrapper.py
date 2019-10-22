# Scrapper module

import requests
import bs4

page = requests.get('https://fr.wikipedia.org/wiki/Django_Unchained')

soup = bs4.BeautifulSoup(page.content, 'html.parser')

def get_title():
    return soup.find('h1').get_text()

