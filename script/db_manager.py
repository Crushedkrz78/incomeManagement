import sqlite3
from sqlite3 import Error

#Database Creation for Testing use
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    create_connection("data\db\pythonsqlite.db")

class dbManager:
    def __init__(self, *args, **kwargs):
        create_conection("data\db\testDB.db")
        return super().__init__(*args, **kwargs)

    def create_conection(db_file):
        """Create a Database connection to a SQLite instance"""
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            conn.close()

    def create_table(conn, create_table_query):
        """ Create a table from a SQL statement
        :param conn: Connection Object
        :param create_table_query: a CREATE TABLE statement
        """

        try:
            c = conn.cursor()
            c.execute(create_table_query)