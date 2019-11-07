class Movie:

    def __init__(self,
                 fr_title,
                 original_title,
                 duration,
                 release_date,
                 rating):
        self.fr_title = fr_title
        self.original_title = original_title
        self.duration = duration
        self.release_date = release_date
        self.rating = rating

        self.id = None
        self.actors = []
        self.productors = []
        self.is_3d = None
        self.production_budget = None
        self.marketing_budget = None

    def total_budget(self):
        if self.production_budget is None or self.marketing_budget is None:
            return None

        return self.production_budget + self.marketing_budget
