from model.DatabasePool import DatabasePool

class movie:

    @classmethod
    def AddOneMovie(cls, jsonMovieBody):
        dbConn=DatabasePool.getConnection()

        try:
            cursor=dbConn.cursor(dictionary=True)
            sql="insert into movie(moviename, description, releasedate, genreid) values(%s, %s, %s, %s)"
            cursor.execute(sql, (jsonMovieBody["moviename"], jsonMovieBody["description"], jsonMovieBody["releasedate"], jsonMovieBody["genreid"]))
            dbConn.commit()
            howmanyrows=cursor.rowcount
            return howmanyrows

        finally:
            dbConn.close()

    @classmethod
    def UpdateOneMovie(cls, jsonMovieBody, id):
        dbConn=DatabasePool.getConnection()

        try:
            cursor=dbConn.cursor(dictionary=True)
            sql="update movie set moviename=%s, description=%s, releasedate=%s, genreid=%s where movieid=%s"
            cursor.execute(sql,(jsonMovieBody["moviename"],jsonMovieBody["description"],jsonMovieBody["releasedate"],jsonMovieBody["genreid"],id))
            dbConn.commit()
            howmanyrows=cursor.rowcount
            return howmanyrows

        finally:
            dbConn.close()

    @classmethod
    def getAllMovies(cls):
        dbConn = DatabasePool.getConnection()
        try:
            cursor = dbConn.cursor(dictionary=True)
            sql = "select * from movie"
            cursor.execute(sql, ())
            movies = cursor.fetchall()
            return movies
        finally:
            dbConn.close()

    @classmethod
    def getMoviesByID(cls, movieid):
        dbConn = DatabasePool.getConnection()
        try:
            cursor = dbConn.cursor(dictionary=True)
            sql = "select * from movie where movieid=%s"
            cursor.execute(sql, (movieid,))
            movies = cursor.fetchall()
            return movies
        finally:
            dbConn.close()

    @classmethod
    def deleteMovie(cls, movieid):
        dbConn = DatabasePool.getConnection()

        try:

            cursor = dbConn.cursor(dictionary=True)
            sql = "delete from movie where movieid=%s"
            cursor.execute(sql, (movieid,))
            dbConn.commit()
            rows = cursor.rowcount
            return rows

        finally:
            dbConn.close()