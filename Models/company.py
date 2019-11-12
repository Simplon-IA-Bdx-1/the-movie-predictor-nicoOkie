class Company:
    def __init__(self, company):
        self.id = company.get("id")
        self.name = company.get("name")
