# Scrapper module

import requests
import bs4
from datetime import datetime as dt
import locale

locale.setlocale(locale.LC_ALL, "fr_FR")

page = requests.get("https://fr.wikipedia.org/wiki/Joker_(film,_2019)")

soup = bs4.BeautifulSoup(page.text, "html.parser")

fiche_tag = soup.find(id="Fiche_technique")
h2_tag = fiche_tag.parent
ul_tag = h2_tag.find_next_sibling("ul")
li_tags = ul_tag.find_all("li", recursive=False)

for li_tag in li_tags:
    splitted_li = li_tag.get_text().split(":")
    data_type = splitted_li[0].strip()
    data_value = splitted_li[1].strip()

    if data_type == "Titre original":
        original_title = data_value

    if data_type == "Durée":
        duration = data_value.replace("minutes", "").strip()

    if data_type == "Dates de sortie":
        release_dates_li_list = li_tag.find_all("li")
        for release_date_li in release_dates_li_list:
            release_date_splitted = release_date_li.get_text().split(":")
            release_date_country = release_date_splitted[0].strip()
            release_date_as_string = release_date_splitted[1].strip()
            if release_date_country == "France":
                release_date_object = dt.strptime(
                    release_date_as_string, "%d %B %Y"
                )
                release_date_sql_string = release_date_object.strftime(
                    "%Y-%m-%d"
                )

    if data_type == "Classification":
        rating_li_list = li_tag.find_all("li")
        for rating_li in rating_li_list:
            rating_splitted = rating_li.get_text().split(":")
            rating_country = rating_splitted[0].strip()
            rating_string = rating_splitted[1].strip()
            if rating_country == "France":
                if rating_string.find("12") != -1:
                    rating = "-12"


print("title = ", original_title)
print("duration = ", duration)
print("release_date = ", release_date_sql_string)
print("rating = ", rating)


exit()

# title, original_title, duration, release_date, rating

# def get_title():
#     return soup.find('h1').get_text()

# def get_lis():
#     return soup.find_all('li')

# def get_original_title():
#     lis = get_lis()
#     for li in lis:
#         if 'Titre original' in li.contents[0]:
#              return li.contents[1].contents[0].get_text()

# # def get_duration():

# def get_release_date():
#     lis = get_lis()
#     for li in lis:
#         if 'Date de sortie' in li.contents[0]:
#             ul = li.contents[1]
#             return ul.contents[0].find('time')['datetime']

# def get_rating():
#     lis = get_lis()
#     for li in lis:
#         if 'Classification' in li.contents[0]:
#             ul = li.find('ul')
#             print(ul.find_all('li'))

# print(get_title())
# print(get_original_title())
# print(get_release_date())


# get_rating()
