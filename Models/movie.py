class Movie:

    def __init__(self,
                 id=None,
                 fr_title=None,
                 original_title=None,
                 duration=None,
                 release_date=None,
                 rating=None,
                 actors=[],
                 productors=[],
                 production_budget=None,
                 marketing_budget=None,
                 is_3d=None):
        self.id = id
        self.fr_title = fr_title
        self.original_title = original_title
        self.duration = duration
        self.release_date = release_date
        self.rating = rating
        self.actors = actors
        self.productors = productors
        self.production_budget = production_budget
        self.marketing_budget = marketing_budget
        self.is_3d = is_3d

    def total_budget(self):
        if self.production_budget is None or self.marketing_budget is None:
            return None

        return self.production_budget + self.marketing_budget
