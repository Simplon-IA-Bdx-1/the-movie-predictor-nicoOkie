import os
import requests


class OpenMovieDb:
    def __init__(self, id):

        # self.TMDB_API_KEY = os.getenv('TMDB_API_KEY')
        self.base_url = f"http://www.omdbapi.com/"
        self.base_params = f"?apikey={os.environ['OMDB_API_KEY']}&"
        self.options_params = f"i={self.id}"
        self.id = id

    def get_tmdb_movie(self):
        return requests.get(self.base_url
                            + self.base_params
                            + self.options_params).json()
