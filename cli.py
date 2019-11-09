import argparse
import sys
# import csv


class Parser(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description="The Moviepredictor CLI",
            usage='''app.py <context> <command> [<args>]

The context can be: people | movie
The commands are:
    list        List the entities
    find        Find one entity by Id
    import      Create DB entries from external sources
    insert      Insert one enity by hand
    scrap       Scrap the web with a URL
''')
        parser.add_argument("context",
                            help="""The context in
                                wich the command will be execute""")
        parser.add_argument("command",
                            help="The command to run")
        args = parser.parse_args(sys.argv[1:3])
        self.context = args.context
        self.command = args.command

        getattr(self, args.command)()

    def list_entities(self):
        parser = argparse.ArgumentParser(
            description="List the entities in database"
        )
        parser.add_argument("--export",
                            help="""Chemin vers le fichier
                                a exporter, format csv""")
        args = parser.parse_args(sys.argv[3:])
        if self.context == "people":
            # people = db.find_all("people")
            if args.export:
                print("people list export")
                # with open(args.export,
                #    'w',
            #       encoding='utf-8',
                #    newline='\n') as csvfile:
                #     writer = csv.writer(csvfile)
                #     writer.writerow(people[0].keys())
                #     for person in people:
                #         writer.writerow(person.values())
            else:
                print("people list")
                # for person in people:
                #     db.print_person(person)
        if self.context == "movies":
            # people = db.find_all("people")
            if args.export:
                print("movies list export")
                # with open(args.export,
                #   'w',
                #   encoding='utf-8',
                #   newline='\n') as csvfile:
                #     writer = csv.writer(csvfile)
                #     writer.writerow(people[0].keys())
                #     for person in people:
                #         writer.writerow(person.values())
            else:
                print("movies list")
                # for person in people:
                #     db.print_person(person)

    def find(self):
        parser = argparse.ArgumentParser(
            description="Find an entity by ID"
        )
        parser.add_argument("id", help="The entity to find's ID")
        args = parser.parse_args(sys.argv[3:])
        if self.context == "people":
            # people_id = args.id
            # people = db.find("people", people_id)
            # for person in people:
            #     db.print_person(person)
            print(f"find people with id: {args.id}")
        if self.context == "movies":
            # movie_id = args.id
            # movies = db.find("movies", movie_id)
            # for movie in movies:
            #     db.print_movie(movie)
            print(f"find movie with id: {args.id}")

    def import_entity(self):
        print("import")

    def insert(self):
        print("insert")
