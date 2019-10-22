#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
TheMoviePredictor script
Author: Arnaud de Mouhy <arnaud@admds.net>
"""

import mysql.connector
import sys
import argparse
import csv

def connectToDatabase():
    return mysql.connector.connect(user='predictor', password='predictor',
                              host='127.0.0.1',
                              database='predictor')

def disconnectDatabase(cnx):
    cnx.close()

def createCursor(cnx):
    return cnx.cursor(dictionary=True)

def closeCursor(cursor):    
    cursor.close()

def findQuery(table, id):
    return ("SELECT * FROM {} WHERE id = {}".format(table, id))

def findAllQuery(table):
    return ("SELECT * FROM {}".format(table))

def insertPeopleQuery(firstname, lastname):
    return ("INSERT INTO  `people` (`firstname`, `lastname`) VALUES  ('{}', '{}')".format(firstname, lastname))

def insertMovieQuery(title, originalTitle, duration, releaseDate, rating):
    return ("INSERT INTO `movies` (`title`, `original_title`, `duration`, `release_date`, `rating`) VALUES ('{}', '{}', {}, '{}', '{}')".format(title, originalTitle, duration, releaseDate, rating))

def find(table, id):
    cnx = connectToDatabase()
    cursor = createCursor(cnx)
    query = findQuery(table, id)
    cursor.execute(query)
    results = cursor.fetchall()
    closeCursor(cursor)
    disconnectDatabase(cnx)
    return results

def findAll(table):
    cnx = connectToDatabase()
    cursor = createCursor(cnx)
    cursor.execute(findAllQuery(table))
    results = cursor.fetchall()
    closeCursor(cursor)
    disconnectDatabase(cnx)
    return results

def insertPeople(firstname, lastname):
    cnx = connectToDatabase()
    cursor = createCursor(cnx)
    query = insertPeopleQuery(firstname, lastname)
    cursor.execute(query)
    cnx.commit()
    closeCursor(cursor)
    disconnectDatabase(cnx)

def insertMovie(title, originalTitle, duration, releaseDate, rating):
    cnx = connectToDatabase()
    cursor = createCursor(cnx)
    query = insertMovieQuery(title, originalTitle, duration, releaseDate, rating)
    cursor.execute(query)
    cnx.commit()
    closeCursor(cursor)
    disconnectDatabase(cnx)

def printPerson(person):
    print("#{}: {} {}".format(person['id'], person['firstname'], person['lastname']))

def printMovie(movie):
    print("#{}: {} released on {}".format(movie['id'], movie['title'], movie['release_date']))

parser = argparse.ArgumentParser(description='Process MoviePredictor data')

parser.add_argument('context', choices=('people', 'movies'), help='Le contexte dans lequel nous allons travailler')

action_subparser = parser.add_subparsers(title='action', dest='action')

list_parser = action_subparser.add_parser('list', help='Liste les entitÃ©es du contexte')
list_parser.add_argument('--export' , help='Chemin du fichier exportÃ©')

find_parser = action_subparser.add_parser('find', help='Trouve une entitÃ© selon un paramÃ¨tre')
find_parser.add_argument('id' , help='Identifant Ã  rechercher')

import_parser = action_subparser.add_parser('import', help='Chemin du fichier a importer')
import_parser.add_argument('--file', help='Le nom du fichier a importer', required=True)

insert_parser = action_subparser.add_parser('insert', help='Insérer des entités du contexte')
intermediateParser = parser.parse_known_args()
commandContex = intermediateParser[0].context
# People Insert
if commandContex == 'people':
    insert_parser.add_argument('--firstname', help='Un prénom', required=True)
    insert_parser.add_argument('--lastname', help='Un nom de famille', required=True)
# Movie Insert
if commandContex == 'movies':
    insert_parser.add_argument('--title', help='Le titre du film', required=True)
    insert_parser.add_argument('--duration', help='La duree du film en minutes', required=True)
    insert_parser.add_argument('--original-title', help='Le titre original du film', required=True)
    insert_parser.add_argument('--release-date', help='La date de sortie du film', required=True)
    insert_parser.add_argument('--rating', help='Limitations de public du film', choices=('TP', '-12', '-16', '-18'), required=True)

args = parser.parse_args()

# print(args)
# exit()

if args.context == "people":
    if args.action == "list":
        people = findAll("people")
        if args.export:
            with open(args.export, 'w', encoding='utf-8', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(people[0].keys())
                for person in people:
                    writer.writerow(person.values())
        else:
            for person in people:
                printPerson(person)
    if args.action == "find":
        peopleId = args.id
        people = find("people", peopleId)
        for person in people:
            printPerson(person)
    if args.action == 'insert':
        peopleFirstname = args.firstname
        peopleLastname = args.lastname
        insertPeople(peopleFirstname, peopleLastname)

if args.context == "movies":
    if args.action == "list":  
        movies = findAll("movies")
        for movie in movies:
            printMovie(movie)
    if args.action == "find":  
        movieId = args.id
        movies = find("movies", movieId)
        for movie in movies:
            printMovie(movie)
    if args.action == "insert":
        title = args.title
        originalTitle = args.original_title
        duration = args.duration
        releaseDate = args.release_date
        rating = args.rating
        insertMovie(title, originalTitle, duration, releaseDate, rating)
    if args.action == "import":
        csvFile = args.file
        with open(csvFile, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                insertMovie(row['title'], row['original_title'], row['duration'], row['release_date'], row['rating'])
