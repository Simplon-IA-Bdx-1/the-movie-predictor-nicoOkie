import requests
import bs4
import locale
from datetime import datetime as dt

# locale.setlocale(locale.LC_ALL, "fr_FR")
class Scraper:
    def __init__(self, url):
        page = requests.get(url,
                        headers={"Accept-Language": "fr, fr-FR"})
        soup = bs4.BeautifulSoup(page.text, "html.parser")
        self.film_infos = soup.find("div", class_="title_wrapper")
        self.synopsis = soup.find("div", class_="inline canwrap").find_next("span").get_text().strip()

    def get_fr_title(self):
        return self.film_infos.find("h1").contents[0]

    def get_original_title(self):
        original_title_full = self.film_infos.find("div", class_="originalTitle")
        if original_title_full is not None:
            return self.film_infos.find("div", class_="originalTitle").contents[0]
        else:
            return self.get_fr_title()

    def get_release_date(self):
        release_date_and_country = self.film_infos.find("a", title="See more release dates").contents[0]
        release_date_as_string = release_date_and_country.split("(")[0].strip()
        return str(dt.strptime(release_date_as_string, "%d %B %Y")).split(" ")[0]

    def get_duration(self):
        return self.film_infos.find("time")["datetime"].replace("PT", "").replace("M", "")

    def get_rating(self):
        rating_string = self.film_infos.find("div", class_="subtext").contents[0].strip()
        if rating_string == "Tous publics":
            return "TP"
        if rating_string == "12":
            return "-12"
        if rating_string == "16":
            return "-16"
        if rating_string == "18":
            return "-18"

    def get_synopsis(self):
        return self.synopsis.replace("'", '"')

# scraper = Scraper("https://www.imdb.com/title/tt0110912")
# print(scraper.get_synopsis())