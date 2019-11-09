"""
TheMoviePredictor script
Author: Arnaud de Mouhy <arnaud@admds.net>
"""
# Modules Imports
import mysql.connector
import argparse
# import csv
# import imdb_scraper
import os

# Local Imports
from cli import Parser
from factory import Factory


def connect_to_database():
    password = os.environ['MYSQL_PASSWORD']
    return mysql.connector.connect(user='predictor',
                                   password=password,
                                   host='database',
                                   database='predictor')


def disconnect_database(cnx):
    cnx.close()


def create_cursor(cnx):
    return cnx.cursor(dictionary=True)


def close_cursor(cursor):
    cursor.close()


def find_query(table, id):
    return ("SELECT * FROM {} WHERE id = {};".format(table, id))


def find_all_query(table):
    return ("SELECT * FROM {};".format(table))


def insert_people_query(firstname, lastname):
    return f"""INSERT INTO  `people` (`firstname`,`lastname`)
            VALUES ('{firstname}', '{lastname}');"""


def insert_movie_query(title,
                       original_title,
                       duration,
                       release_date,
                       rating,
                       synopsis=None):
    return f"""INSERT INTO `movies`
            (`title`,
             `original_title`,
             `synopsis`,
             `duration`,
             `release_date`,
             `rating`)
             VALUES ('{title}',
             '{original_title}',
             '{synopsis}',
             '{duration}',
             '{release_date}',
             '{rating}')"""


def find(table, id):
    cnx = connect_to_database()
    cursor = create_cursor(cnx)
    query = find_query(table, id)
    cursor.execute(query)
    results = cursor.fetchall()
    close_cursor(cursor)
    disconnect_database(cnx)
    return results


def find_all(table):
    cnx = connect_to_database()
    cursor = create_cursor(cnx)
    cursor.execute(find_all_query(table))
    results = cursor.fetchall()
    close_cursor(cursor)
    disconnect_database(cnx)
    return results


def insert_people(firstname, lastname):
    cnx = connect_to_database()
    cursor = create_cursor(cnx)
    query = insert_people_query(firstname, lastname)
    cursor.execute(query)
    cnx.commit()
    close_cursor(cursor)
    disconnect_database(cnx)


def insert_movie(title,
                 original_title,
                 duration,
                 release_date,
                 rating,
                 synopsis=None):
    cnx = connect_to_database()
    cursor = create_cursor(cnx)
    query = insert_movie_query(title,
                               original_title,
                               duration,
                               release_date,
                               rating,
                               synopsis)
    cursor.execute(query)
    cnx.commit()
    close_cursor(cursor)
    disconnect_database(cnx)


# def print_person(person):
#     print("#{}: {} {}".format(person['id'],
#                               person['firstname'],
#                               person['lastname']))


# def print_movie(movie):
#     print("#{}: {} released on {}".format(movie['id'],
#                                           movie['title'],
#                                           movie['release_date']))


# parser = Parser()

parser = argparse.ArgumentParser(description='Process MoviePredictor data')

parser.add_argument('context', choices=('people', 'movies'),
                    help='Le contexte dans lequel nous allons travailler')

intermediateParser = parser.parse_known_args()
commandContex = intermediateParser[0].context

action_subparser = parser.add_subparsers(title='action', dest='action')

# List
list_parser = action_subparser.add_parser('list',
                                          help='Liste les entitÃ©es du contexte')
list_parser.add_argument('--export', help='Chemin du fichier exportÃ©')

# Find
find_parser = action_subparser.add_parser('find',
                                          help='Trouve une entitÃ© selon un paramÃ¨tre')
find_parser.add_argument('id', help='Identifant Ã  rechercher')

# Import
import_parser = action_subparser.add_parser('import',
                                            help='Chemin du fichier a importer')
import_parser.add_argument('--file', help='Le nom du fichier a importer',
                           required=True)

# Insert
insert_parser = action_subparser.add_parser('insert',
                                            help='Insérer des entités du contexte')
# People
if commandContex == 'people':
    insert_parser.add_argument('--firstname',
help='Un prénom', required=True)
    insert_parser.add_argument('--lastname',
help='Un nom de famille', required=True)
# Movie
if commandContex == 'movies':
    insert_parser.add_argument('--title',
help='Le titre du film', required=True)
    insert_parser.add_argument('--duration',
help='La duree du film en minutes', required=True)
    insert_parser.add_argument('--original-title',
help='Le titre original du film', required=True)
    insert_parser.add_argument('--release-date',
 help='La date de sortie du film', required=True)
    insert_parser.add_argument('--rating',
help='Limitations de public du film', choices=('TP', '-12', '-16', '-18'),
required=True)

    # Scraper
    scrap_parser = action_subparser.add_parser('scrap',
help='Importer un film depuis une url IMDB')
    scrap_parser.add_argument('--url',
help='L\'url d\'un film sur IMDB', required=True)

args = parser.parse_args()

# print(args)
# exit()

if args.context == "people":
    if args.action == "list":
        people = find_all("people")
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
    if args.action == "find":
        peopleId = args.id
        people = find("people", peopleId)
        for person in people:
            Factory.print_person(person)
    if args.action == 'insert':
        # peopleFirstname = args.firstname
        # peopleLastname = args.lastname
        # insert_people(peopleFirstname, peopleLastname)
        insert_people(firstname=args.firstname, lastname=args.lastname)

if args.context == "movies":
    if args.action == "list":
        movies = find_all("movies")
        for movie in movies:
            Factory.print_movie(movie)
    if args.action == "find":
        movieId = args.id
        movies = find("movies", movieId)
        for movie in movies:
            Factory.print_movie(movie)
    if args.action == "insert":
        title = args.title
        original_title = args.original_title
        duration = args.duration
        release_date = args.release_date
        rating = args.rating
        insert_movie(title, original_title, duration, release_date, rating)
    if args.action == "import":
        csvFile = args.file
        with open(csvFile, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                insert_movie(row['title'], row['original_title'],
row['duration'], row['release_date'], row['rating'])
    if args.action == "scrap":
        scraper = imdb_scraper.Scraper(args.url)
        insert_movie(scraper.get_fr_title(), scraper.get_original_title(),
scraper.get_duration(), scraper.get_release_date(), scraper.get_rating(),
scraper.get_synopsis())
