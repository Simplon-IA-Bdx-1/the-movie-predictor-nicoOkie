# Scrapper module

import requests
import bs4

page = requests.get('https://fr.wikipedia.org/wiki/Django_Unchained')

soup = bs4.BeautifulSoup(page.content, 'html.parser')

# title, original_title, duration, release_date, rating

def get_title():
    return soup.find('h1').get_text()

def get_original_title():
    lis = soup.find_all('li')
    for li in lis:
        if 'Titre original' in li.contents[0]:
             return li.contents[1].contents[0].contents[0]

# def get_duration():

# def get_release_date():

# def get_rating():
