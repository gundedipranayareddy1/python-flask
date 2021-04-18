import sqlite3


def get_db_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect('database.sqlite')
        print("Opened database successfully")
    except sqlite3.Error as e:
        print(e)

    return conn




