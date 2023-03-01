from model.DatabasePool import DatabasePool
from settings.settings import Settings
from dotenv import load_dotenv
import jwt
import datetime
from flask import request, jsonify, Flask, g

class user:
    

    @classmethod
    def login(cls, jsonUserBody):
        dbConn = DatabasePool.getConnection()

        try:

            cursor = dbConn.cursor(dictionary=True)
            sql = "select * from users where email=%s and password=%s"
            cursor.execute(sql, (jsonUserBody["email"], jsonUserBody["password"]))
            users = cursor.fetchall()

            if len(users) == 0:
                return "No such user"
            else:
                payload = {"email": users[0]["email"], "role": users[0]["role"],
                           "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=7200)}
                token = jwt.encode(
                    payload, Settings.secretKey, algorithm="HS256")
                return token

        finally:
            dbConn.close()

    @classmethod
    def Insertuser(cls,jsonUserBody):
        dbConn = DatabasePool.getConnection()

        try:

            cursor = dbConn.cursor(dictionary=True)
            sql = "insert into users(email,password) values(%s,%s)"
            cursor.execute(sql,(jsonUserBody["email"],jsonUserBody["password"]))
            dbConn.commit()
            rows=cursor.rowcount
            return rows

        finally:
            dbConn.close()