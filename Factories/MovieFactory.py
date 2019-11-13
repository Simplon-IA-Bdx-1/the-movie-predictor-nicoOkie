import database
from Models.movie import Movie

db = database.Database()


class MovieFactory:
    # INSERT
    def insert_query(movie):
        statement = """INSERT INTO `movies` (`fr_title`,
                                        `original_title`,
                                        `synopsis`,
                                        `duration`,
                                        `release_date`,
                                        `adult`,
                                        `budget`,
                                        `imdb_id`,
                                        `score`)
                                        VALUES (%s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s)"""
        data = (movie.fr_title, movie.original_title,
                movie.synopsis, movie.duration,
                movie.release_date, movie.adult,
                movie.budget, movie.imdb_id, movie.score)
        return (statement, data)

    @staticmethod
    def insert(movie):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        statement, data = MovieFactory.insert_query(movie)
        movie = MovieFactory.get(movie)
        if movie:
            return movie.id
        cursor.execute(statement, data)
        cnx.commit()
        inserted_id = cursor.lastrowid
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        return inserted_id

    # GET
    def get_query(movie):
        statement = """SELECT * FROM `movies` WHERE `fr_title` = %s"""
        data = (movie.fr_title,)
        return (statement, data)

    @staticmethod
    def get(movie):
        cnx = db.connect_to_database()
        cursor = db.create_cursor(cnx)
        statement, data = MovieFactory.get_query(movie)
        cursor.execute(statement, data)
        results = cursor.fetchall()
        db.close_cursor(cursor)
        db.disconnect_database(cnx)
        if results:
            return Movie(results[0])
        return None
