import database

db = database.Database()


class Factory:

    # INSERT FONCTIONS
    @staticmethod
    def insert_movie_query(title,
                           original_title,
                           duration,
                           release_date,
                           rating,
                           synopsis="NULL"):
        return ("""INSERT INTO `movies` (`title`,
                                        `original_title`,
                                        `synopsis`,
                                        `duration`,
                                        `release_date`,
                                        `rating`)
                                        VALUES (f'{title}',
                                                f'{original_title}',
                                                f'{synopsis}',
                                                f'{duration}',
                                                f'{release_date}',
                                                f'{rating}')""")

    @staticmethod
    def insert_people_query(firstname, lastname):
        return ("""INSERT INTO  `people` (`firstname`,
                                          `lastname`)
                                          VALUES  (f'{firstname}',
                                                   f'{lastname}');""")

    @staticmethod
    def insert_companies_query(name):
        return ("INSERT INTO `companies` (`name`) VALUES (f'{name}')")

    @staticmethod
    def insert_roles_query(name):
        return ("INSERT INTO `roles` (`name`) VALUES (f'{name}')")

    # LIST FONCTIONS
    @staticmethod
    def find_query(table, id):
        return (f"SELECT * FROM {table} WHERE id = {id};")

    @staticmethod
    def find(table, id):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        query = db.find_query(table, id)
        cursor.execute(query)
        results = cursor.fetchall()
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return results

    @staticmethod
    def find_all_query(table):
        return ("SELECT * FROM {table};")

    @staticmethod
    def find_all(table):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        cursor.execute(Factory.find_all_query(table))
        results = cursor.fetchall()
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return results

    # PRINT FONCTIONS
    @staticmethod
    def print_person(person):
        print("#{}: {} {}".format(person['id'],
                                  person['firstname'],
                                  person['lastname']))

    @staticmethod
    def print_movie(movie):
        print("""#{movie['id']}:
            {movie['fr_title']} released on {movie['release_date']}""")
