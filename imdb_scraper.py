import requests
import bs4
import locale
from datetime import datetime as dt

# locale.setlocale(locale.LC_ALL, "fr_FR")

page = requests.get("https://www.imdb.com/title/tt0071853/",
                    headers={"Accept-Language": "fr, fr-FR"})
soup = bs4.BeautifulSoup(page.text, "html.parser")

film_infos = soup.find("div", class_="title_wrapper")

def get_fr_title():
    return film_infos.find("h1").contents[0]

def get_original_title():
    original_title_full = film_infos.find("div", class_="originalTitle")
    if original_title_full is not None:
        return film_infos.find("div", class_="originalTitle").contents[0]
    else:
        return get_fr_title()

def get_release_date():
    release_date_and_country = film_infos.find("a", title="See more release dates").contents[0]
    release_date_as_string = release_date_and_country.split("(")[0].strip()
    return str(dt.strptime(release_date_as_string, "%d %B %Y")).split(" ")[0]

def get_duration():
    return film_infos.find("time")["datetime"].replace("PT", "").replace("M", "")

def get_rating():
    rating_string = film_infos.find("div", class_="subtext").contents[0].strip()
    if rating_string == "Tous publics":
        return "TP"
    if rating_string == "12":
        return "-12"
    if rating_string == "16":
        return "-16"
    if rating_string == "18":
        return "-18"

print(get_fr_title(), get_original_title(), get_release_date(), get_duration(), get_rating())
