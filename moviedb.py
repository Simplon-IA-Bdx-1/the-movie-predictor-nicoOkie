from os import environ
import requests

class MovieDB:


    def __init__(self, default=lambda self: self.env.user.id):
        # General Config:
        self.TMDB_API_KEY = environ.get('TMDB_API_KEY')
        self.base_url = 'https://api.themoviedb.org/3'

        self.id = id


    def autentication(self):
        return "Authorization: Bearer" + self.TMDB_API_KEY

    def get_movie(self):
        r = requests.get(self.base_url + f"/movie/{self.id}")
        print(r.json)


mdb = MovieDB

mdb.get_movie('tt0081505')