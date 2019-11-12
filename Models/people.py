class People:
    def __init__(self, person):
        self.id = person.get("id")
        self.firstname = person.get("firstname")
        self.lastname = person.get("lastname")
