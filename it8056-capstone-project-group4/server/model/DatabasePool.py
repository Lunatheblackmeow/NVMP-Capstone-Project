import os
from dotenv import load_dotenv
from mysql.connector import pooling

load_dotenv()

# Create pool with these variables
# Remember to specify their values in .env first (See README on creating .env)
host = os.getenv('DB_HOST')
database = os.getenv('DB_DATABASE')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

class DatabasePool:
    #class variable
    # print( os.getenv('DB_USER')) for testing
    # print( os.getenv('DB_PASSWORD')) for testing
    connection_pool = pooling.MySQLConnectionPool(pool_name="ws_pool",
                                                  pool_size=5,
                                                  host=os.getenv('DB_HOST'),
                                                  database=os.getenv('DB_DATABASE'),
                                                  user=os.getenv('DB_USER'),
                                                  password=os.getenv('DB_PASSWORD'))
    
    @classmethod
    def getConnection(cls):
        dbConn = cls.connection_pool.get_connection()
        return dbConn