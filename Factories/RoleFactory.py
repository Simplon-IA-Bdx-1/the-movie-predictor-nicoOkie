from database import Database as db
from Models.role import Role


class RoleFactory:
    def insert_query(role):
        statement = """INSERT INTO  `roles` (`name`)
                                     VALUES  (%s);"""
        data = (role,)
        return (statement, data)

    @staticmethod
    def insert(role):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        statement, data = RoleFactory.insert_query(role)
        role = RoleFactory.get(role)
        if role:
            return role.id
        cursor.execute(statement, data)
        cnx.commit()
        inserted_id = cursor.lastrowid
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return inserted_id

    def insert_mpr_query(person, movie_id):
        statement = f"""INSERT INTO `movies_people_roles` (`movie_id`,
                                                `people_id`,
                                                `role_id`)
                        VALUES (%s, %s, %s);"""
        data = (movie_id, person[0], person[1])
        return (statement, data)

    @staticmethod
    def insert_mpr(person, movie_id):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        statement, data = RoleFactory.insert_mpr_query(person, movie_id)
        mpr = RoleFactory.get_mpr(person, movie_id)
        if mpr:
            return "We already know this person is in this movie"
        cursor.execute(statement, data)
        cnx.commit()
        inserted_id = cursor.lastrowid
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return inserted_id

    def insert_mcr_query(company, movie_id):
        statement = f"""INSERT INTO `movies_companies_roles` (`movie_id`,
                                                `company_id`,
                                                `role_id`)
                        VALUES (%s, %s, %s);"""
        data = (movie_id, company[0], company[1])
        return (statement, data)

    @staticmethod
    def insert_mcr(company, movie_id):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        statement, data = RoleFactory.insert_mcr_query(company, movie_id)
        mcr = RoleFactory.get_mcr(company, movie_id)
        if mcr:
            return "We already know this company is in this movie"
        cursor.execute(statement, data)
        cnx.commit()
        inserted_id = cursor.lastrowid
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return inserted_id

    def get_query(role):
        statement = """SELECT * FROM `roles`
                        WHERE `name` = %s;"""
        data = (role,)
        return (statement, data)

    @staticmethod
    def get(role):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        statement, data = RoleFactory.get_query(role)
        cursor.execute(statement, data)
        results = cursor.fetchall()
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        if results:
            return Role(results[0])
        return None

    def get_mpr_query(person, movie_id):
        statement = f"""SELECT * FROM `movies_people_roles`
                        WHERE `movie_id` = %s
                        AND `people_id` = %s
                        AND `role_id` = %s;"""
        data = (movie_id, person[0], person[1])
        return (statement, data)

    @staticmethod
    def get_mpr(person, movie_id):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        statement, data = RoleFactory.get_mpr_query(person, movie_id)
        cursor.execute(statement, data)
        results = cursor.fetchall()
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return results

    def get_mcr_query(company, movie_id):
        statement = f"""SELECT * FROM `movies_companies_roles`
                        WHERE `movie_id` = %s
                        AND `company_id` = %s
                        AND `role_id` = %s;"""
        data = (movie_id, company[0], company[1])
        return (statement, data)

    @staticmethod
    def get_mcr(company, movie_id):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        statement, data = RoleFactory.get_mcr_query(company, movie_id)
        cursor.execute(statement, data)
        results = cursor.fetchall()
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return results
