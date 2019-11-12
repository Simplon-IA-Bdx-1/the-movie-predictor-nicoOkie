from database import Database as db
from Models.people import People


class PeopleFactory:
    # INSERT
    def insert_query(person):
        statement = """INSERT INTO  `people` (`firstname`, `lastname`)
                                     VALUES  (%s, %s);"""
        data = (person.firstname, person.lastname)
        return (statement, data)

    @staticmethod
    def insert(person):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        statement, data = PeopleFactory.insert_query(person)
        person = PeopleFactory.get(person)
        if person:
            return person.id
        cursor.execute(statement, data)
        cnx.commit()
        inserted_id = cursor.lastrowid
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return inserted_id

    # GET
    def get_query(person):
        statement = """SELECT * FROM `people`
                        WHERE `firstname` = %s
                        AND `lastname` = %s;"""
        data = (person.firstname, person.lastname)
        return (statement, data)

    @staticmethod
    def get(person):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        statement, data = PeopleFactory.get_query(person)
        cursor.execute(statement, data)
        results = cursor.fetchall()
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        for result in results:
            return People(result)
        return None
