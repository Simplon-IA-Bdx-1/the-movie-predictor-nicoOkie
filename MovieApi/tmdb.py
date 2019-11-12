import os
import requests

import utils


class TheMovieDb:
    def __init__(self, id):
        self.base_url = f"https://api.themoviedb.org/3/movie/{id}"
        self.credits = "?&append_to_response=credits"
        self.language = "&language=fr_FR"
        self.headers = {
            "Authorization": f"Bearer {os.environ['TMDB_API_KEY']}",
        }

    def get_tmdb_movie(self):
        return requests.get(self.base_url
                            + self.credits
                            + self.language,
                            headers=self.headers).json()

    def make_movie(self, data):
        return {
            "budget": data["budget"],
            "imdb_id": data["imdb_id"],
            "fr_title": data["title"],
            "original_title": data["original_title"],
            "duration": data["runtime"],
            "release_date": data["release_date"],
            "adult": data["adult"],
            "synopsis": data["overview"],
            "score": data["vote_average"],
        }

    def make_actor(self, data):
        raw_actors = data["credits"]["cast"]
        actors = []
        for actor in raw_actors:
            firstname, lastname = utils.split_name(actor["name"])
            actor = {
                "firstname": firstname,
                "lastname": lastname,
            }
            actors.append(actor)
        return actors

    def make_crew(self, data):
        raw_crew = data["credits"]["crew"]
        crew = []
        for person in raw_crew:
            firstname, lastname = utils.split_name(person["name"])
            person = {
                "firstname": firstname,
                "lastname": lastname,
                "role": person["job"]
            }
            crew.append(person)
        return crew

    def make_company(self, data):
        raw_companies = data["production_companies"]
        companies = []
        for entity in raw_companies:
            company = {
                "name": entity["name"]
            }
            companies.append(company)
        return companies
