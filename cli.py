import argparse
import sys
import csv

# Local Imports
from Factories.factory import Factory
from Models.movie import Movie
from Factories.MovieFactory import MovieFactory
from MovieApi.tmdb import TheMovieDb as tmdb


class Parser(object):
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="The Moviepredictor CLI",
            usage="""app.py <context> <command> [<args>]

The context can be: people | movie
The commands are:
    list        List the entities
    find        Find one entity by Id
    import      Create DB entries from external sources
    insert      Insert one enity by hand
    scrap       Scrap the web with a URL
""",
        )
        parser.add_argument(
            "context",
            help="""The context in
                    wich the command will be execute""",
        )
        parser.add_argument("command", help="The command to run")
        args = parser.parse_args(sys.argv[1:3])
        self.context = args.context
        self.command = args.command

        getattr(self, args.command)()

    def list(self):
        parser = argparse.ArgumentParser(
            description="List the entities in database"
        )
        parser.add_argument(
            "--export",
            help="""Chemin vers le fichier
                                a exporter, format csv""",
        )
        args = parser.parse_args(sys.argv[3:])
        if self.context == "people":
            people = Factory.find_all("people")
            if args.export:
                with open(args.export,
                          'w',
                          encoding='utf-8',
                          newline='\n') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(people[0].keys())
                    for person in people:
                        writer.writerow(person.values())
            else:
                for person in people:
                    Factory.print_person(person)
        if self.context == "movies":
            movies = Factory.find_all("movies")
            if args.export:
                with open(args.export,
                          'w',
                          encoding='utf-8',
                          newline='\n') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(movies[0].keys())
                    for movie in movies:
                        writer.writerow(movie.values())
            else:
                for movie in movies:
                    Factory.print_movie(movie)

    def find(self):
        parser = argparse.ArgumentParser(description="Find an entity by ID")
        parser.add_argument("id", help="The entity to find's ID")
        args = parser.parse_args(sys.argv[3:])
        if self.context == "people":
            # people_id = args.id
            # people = db.find("people", people_id)
            # for person in people:
            #     db.print_person(person)
            print(f"find people with id: {args.id}")
        if self.context == "movies":
            movie_id = args.id
            movies = Factory.find("movies", movie_id)
            for movie in movies:
                Factory.print_movie(movie)

    def insert(self):
        parser = argparse.ArgumentParser(
            description="Insert a new entity in database"
        )
        if self.context == "people":
            parser.add_argument(
                "--firstname",
                help="Un prénom",
                required=True
            )
            parser.add_argument(
                "--lastname",
                help="Un nom de famille",
                required=True
            )
            args = parser.parse_args(sys.argv[3:])
        if self.context == "movies":
            parser.add_argument(
                "--api",
                help="Le type d'api a utiliser"
            )
            parser.add_argument(
                "imdb_id",
                help="The IMDB movie_id"
            )
            parser.add_argument(
                "--title",
                help="Le titre du film",
                )
            parser.add_argument(
                "--duration",
                help="La duree du film en minutes",
                )
            parser.add_argument(
                "--original-title",
                help="Le titre original du film",
                )
            parser.add_argument(
                "--release-date",
                help="La date de sortie du film",
                )
            parser.add_argument(
                "--rating",
                help="Limitations de public du film",
                choices=("TP", "-12", "-16", "-18"),
                )
            args = parser.parse_args(sys.argv[3:])
            if args.api == "tmdb":
                api = tmdb(args.imdb_id)
                data = api.get_tmdb_movie()
                movie = api.make_movie(data)
                cast = api.make_actor(data)
                crew = api.make_crew(data)
                companies = api.make_company(data)
                movie_data = {
                    "movie": movie,
                    "cast": cast,
                    "crew": crew,
                    "companies": companies,
                }
                Factory.insert_all(movie_data)
                return print("Get a movie and inserted it")
            movie = {
                "fr_title": args.title,
                "duration": args.duration,
                "original_title": args.original_title,
                "release_date": args.release_date,
                "rating": args.rating,
            }
            movie = Movie(movie)
            print(f"Movie inserted at id: #{MovieFactory.insert_movie(movie)}")

    def import_entity(self):
        print("import")
