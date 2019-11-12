class Movie:
    def __init__(
        self,
        movie
    ):
        self.id = movie.get("id")
        self.budget = movie.get("budget")
        self.imdb_id = movie.get("imdb_id")
        self.fr_title = movie.get("fr_title")
        self.original_title = movie.get("original_title")
        self.duration = movie.get("duration")
        self.release_date = movie.get("release_date")
        self.adult = movie.get("adult")
        self.synopsis = movie.get("synopsis")
        self.is_3d = movie.get("is_3d")
        self.score = movie.get("score")
