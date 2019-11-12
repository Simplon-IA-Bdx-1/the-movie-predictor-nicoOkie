from database import Database as db
from Models.company import Company


class CompanyFactory:
    def insert_query(company):
        statement = """INSERT INTO  `companies` (`name`)
                                     VALUES  (%s);"""
        data = (company.name,)
        return (statement, data)

    @staticmethod
    def insert(company):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        statement, data = CompanyFactory.insert_query(company)
        company = CompanyFactory.get(company)
        if company:
            return company.id
        cursor.execute(statement, data)
        cnx.commit()
        inserted_id = cursor.lastrowid
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return inserted_id

    def get_query(company):
        statement = """SELECT * FROM `companies`
                        WHERE `name` = %s;"""
        data = (company.name,)
        return (statement, data)

    @staticmethod
    def get(company):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        statement, data = CompanyFactory.get_query(company)
        cursor.execute(statement, data)
        results = cursor.fetchall()
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        if results:
            return Company(results[0])
        return None
