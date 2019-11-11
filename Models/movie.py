class Movie:
    def __init__(
        self,
        id=None,
        imdb_id=None,
        budget=None,
        fr_title=None,
        original_title=None,
        duration=None,
        release_date=None,
        rating=None,
        synopsis=None,
        is_3d=None,
        cast=[],
        crew={},
        companies=[],
    ):
        self.id = id
        self.imdb_id = imdb_id
        self.budget = budget
        self.fr_title = fr_title
        self.original_title = original_title
        self.duration = duration
        self.release_date = release_date
        self.rating = rating
        self.synopsis = synopsis
        self.is_3d = is_3d
        self.cast = cast
        self.crew = crew
        self.companies = companies
