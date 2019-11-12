# Local Imports
import database
from Models.movie import Movie
from Models.people import People
from Models.company import Company
from Models.role import Role

db = database.Database()


class Factory:

    # INSERT FONCTIONS
    # QUERIES
    def insert_movie_query(self, movie):
        insert_movie_statement = """INSERT INTO `movies` (`fr_title`,
                                        `original_title`,
                                        `synopsis`,
                                        `duration`,
                                        `release_date`,
                                        `aduly`)
                                        VALUES (%s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s)"""
        data = (movie.fr_title, movie.original_title,
                movie.synopsis, movie.duration,
                movie.release_date, movie.adult)
        return (insert_movie_statement, data)

    def insert_people_query(self, person):
        insert_people_statement = """INSERT INTO  `people` (`firstname`,
                                                             `lastname`)
                                     VALUES  (%s, %s);"""
        data = (person.firstname, person.lastname)
        return (insert_people_statement, data)

    def insert_companies_query(self, company):
        insert_companies_statement = """INSERT INTO `companies` (`name`)
                                        VALUES (%s)"""
        data = (company.name)
        return (insert_companies_statement, data)

    def insert_roles_query(self, company):
        insert_roles_statement = "INSERT INTO `roles` (`name`) VALUES (%s)"
        data = (company.name)
        return (insert_roles_statement, data)

    def insert_movie_people_role_query(self, movie_id, people_id):
        insert_statement = """INSERT INTO `movies_people_role`
                               VALUES (%s, %s, %s)"""
        data = (movie_id, people_id, 1)
        return (insert_statement, data)

    # INSERTION
    @staticmethod
    def mega_insert(self, entity):
        if isinstance(entity, Movie):
            self.insert_movie(entity)
        if isinstance(entity, People):
            self.insert_people(entity)
        if isinstance(entity, Company):
            self.insert_company(entity)
        if isinstance(entity, Role):
            self.insert_role(entity)

    @staticmethod
    def insert_movie_cast_crew_companies(self, movie):
        movie_id = self.insert_movie(movie)
        actor_ids = []
        crew_ids = []
        company_ids = []

        for actor in movie.cast:
            actor_ids.append(self.insert_people(actor))
        for member in movie.crew:
            crew_ids.append(self.insert_people(member))
        for company in movie.companies:
            company_ids.append(self.insert_company(company))
        for actor_id in actor_ids:
            self.insert_movie_people_role(movie_id, actor_id)

    @staticmethod
    def insert_movie(self, movie):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        query = self.insert_movie_query(movie)
        cursor.execute(query)
        cnx.commit()
        inserted_id = cursor.lastrowid
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return inserted_id

    @staticmethod
    def insert_people(self, person):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        query = self.insert_people_query(person)
        cursor.execute(query)
        cnx.commit()
        inserted_id = cursor.lastrowid
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return inserted_id

    @staticmethod
    def insert_role(self, role):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        query = self.insert_people_query(role)
        cursor.execute(query)
        cnx.commit()
        inserted_id = cursor.lastrowid
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return inserted_id

    @staticmethod
    def insert_company(self, company):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        query = self.insert_company_query(company)
        cursor.execute(query)
        cnx.commit()
        inserted_id = cursor.lastrowid
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return inserted_id

    @staticmethod
    def insert_movie_people_role(self, id):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        query = self.insert_movie_people_role_query(id.movie, id.people)
        cursor.execute(query)
        cnx.commit()
        db.close_cursor(cursor)
        db.disconnect_database(cnx)

    @staticmethod
    def insert_movie_company_role(self, id):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        query = self.insert_company_role_query(id.movie, id.company, id.role)
        cursor.execute(query)
        cnx.commit()
        db.close_cursor(cursor)
        db.disconnect_database(cnx)

    # LIST FONCTIONS
    @staticmethod
    def find_query(self, table, id):
        return f"SELECT * FROM {table} WHERE id = {id};"

    @staticmethod
    def find(self, table, id):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        query = db.find_query(table, id)
        cursor.execute(query)
        results = cursor.fetchall()
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return results

    @staticmethod
    def find_all_query(self, table):
        return f"SELECT * FROM {table};"

    @staticmethod
    def find_all(self, table):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        cursor.execute(self.find_all_query(table))
        results = cursor.fetchall()
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return results

    def get_role_id_query(self, role):
        statement = "SELECT `id` FROM `role` WHERE role = %s"
        data = (role,)
        return (statement, data)

    def get_role_id(self, role):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        cursor.execute(self.get_role_id_query(role))
        results = cursor.fetchall()
        db.close_cursor()
        db.disconnect_database()
        return results

    # PRINT FONCTIONS
    @staticmethod
    def print_person(self, person):
        print(
            "#{}: {} {}".format(
                person["id"], person["firstname"], person["lastname"]
            )
        )

    @staticmethod
    def print_movie(movie):
        print(
            f"""#{movie['id']}:
            {movie['fr_title']} released on {movie['release_date']}"""
        )
