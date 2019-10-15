# Scrapper module

import requests
import bs4

page = requests.get('https://fr.wikipedia.org/wiki/Django_Unchained')

soup = bs4.BeautifulSoup(page.content, 'html.parser')
html = list(soup.children)[2]
body = list(html.children)[3]

def getTextNode(param='', string=''):
    return body.find(param).get_text()

title = getTextNode('h1')
# print(title)

technicalSheetId = body.find(id='Fiche_technique')
for parent in technicalSheetId.parents:
    if parent.name == 'h2':
        technicalSheetH2 = parent

technicalSheetList = technicalSheetH2.next_sibling.next_sibling

print(technicalSheetList)

