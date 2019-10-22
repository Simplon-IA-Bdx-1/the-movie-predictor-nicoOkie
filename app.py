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

def connect_to_database():
    return mysql.connector.connect(user='predictor', password='predictor',
                              host='127.0.0.1',
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
    return ("INSERT INTO  `people` (`firstname`, `lastname`) VALUES  ('{}', '{}');".format(firstname, lastname))

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

def print_person(person):
    print("#{}: {} {}".format(person['id'], person['firstname'], person['lastname']))

def print_movie(movie):
    print("#{}: {} released on {}".format(movie['id'], movie['title'], movie['release_date']))

parser = argparse.ArgumentParser(description='Process MoviePredictor data')

parser.add_argument('context', choices=['people', 'movies'], help='Le contexte dans lequel nous allons travailler')

action_subparser = parser.add_subparsers(title='action', dest='action')

list_parser = action_subparser.add_parser('list', help='Liste les entitÃ©es du contexte')
list_parser.add_argument('--export' , help='Chemin du fichier exportÃ©')

find_parser = action_subparser.add_parser('find', help='Trouve une entitÃ© selon un paramÃ¨tre')
find_parser.add_argument('id' , help='Identifant Ã  rechercher')

insert_parser = action_subparser.add_parser('insert', help='Insérer des entités du contexte')
# People Insert
insert_parser.add_argument('--firstname', help='Un prénom', required=True)
insert_parser.add_argument('--lastname', help='Un nom de famille', required=True)

args = parser.parse_args()

# print(args)

if args.context == "people":
    if args.action == "list":
        people = find_all("people")
        if args.export:
            with open(args.export, 'w', encoding='utf-8', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(people[0].keys())
                for person in people:
                    writer.writerow(person.values())
        else:
            for person in people:
                print_person(person)
    if args.action == "find":
        peopleId = args.id
        people = find("people", peopleId)
        for person in people:
            print_person(person)
    if args.action == 'insert':
        # peopleFirstname = args.firstname
        # peopleLastname = args.lastname
        # insert_people(peopleFirstname, peopleLastname)
        insert_people(firstname=args.firstname, lastname=args.lastname)

if args.context == "movies":
    if args.action == "list":  
        movies = find_all("movies")
        for movie in movies:
            print_movie(movie)
    if args.action == "find":  
        movieId = args.id
        movies = find("movies", movieId)
        for movie in movies:
            print_movie(movie)
