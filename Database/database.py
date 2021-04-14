import sqlite3


def get_db_connection():

    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    print("Opened database successfully")
    return cursor




