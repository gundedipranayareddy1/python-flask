from flask import json, jsonify
from sqlite3 import Error

from Database.database import get_db_connection


# class audioFile():
#     def __init__(self):
#         self.conn = get_db_connection


def create_song(conn, jsonData):

    db = conn.cursor()
    print("entered create_song method")

    id = jsonData['ID']
    name = jsonData['name']
    duration = jsonData['duration']
    uploadedTime = jsonData['uploadedTime']

    create_query = '''CREATE TABLE IF NOT EXISTS SONG
                   (
                   ID INT PRIMARY KEY  not null,
                   NAME TEXT(100),
                   DURATION LONG,
                   UPLOADEDTIME DATETIME
                   )'''
    # insert_query = "INSERT INTO SONGS VALUES(jsondata[audioFileType'],jsonmeta['ID'],jsonmeta['name'],jsonmeta['duration'],jsonmeta['uploadedTime'])"
    # insert_query = '''INSERT INTO SONGS VALUES(4,"hosanaa",2000,"23:23:12")'''
    db.execute(create_query)
    # connection.commit()
    insert_query='''INSERT OR REPLACE INTO SONG(id,name,duration,uploadedtime) VALUES(?,?,?,?)'''
    db.execute(insert_query, [id, name, duration, uploadedTime])
    conn.commit()
    db.execute('''select * from song''')
    values = db.fetchall()
    return "Action is successful,200 OK"



def create_podcast(conn,jsondata):

    db = conn.cursor()
    print("entered create_podcast method")
    id = jsondata['ID']
    name = jsondata['name']
    duration = jsondata['duration']
    uploadedTime = jsondata['uploadedTime']
    host = jsondata['host']
    participantsList = jsondata['participants']
    participants=""
    for i in participantsList:
        participants = participants +","+ i
    participants=participants[:-2]

    create_query = '''CREATE TABLE IF NOT EXISTS PODCAST
                   (
                   ID INT PRIMARY KEY NOT NULL,
                   NAME TEXT(100),
                   DURATION LONG,
                   UPLOADEDTIME DATETIME,
                   HOST TEXT(100),
                   PARTICIPANTS TEXT(1000)
                   )'''

    db.execute(create_query)
    insert_query='''INSERT OR REPLACE INTO PODCAST(id,name,duration,uploadedtime, host, participants) VALUES(?,?,?,?,?,?)'''
    db.execute(insert_query, [id, name, duration, uploadedTime, host, participants])
    conn.commit()
    db.execute('''select * from PODCAST''')
    values = db.fetchall()
    return "Action is successful,200 OK"


def create_audiobook(conn, jsondata):

    db = conn.cursor()
    print("entered create_audiobook method")
    id = jsondata['ID']
    name = jsondata['name']
    duration = jsondata['duration']
    uploadedTime = jsondata['uploadedTime']
    author = jsondata['author']
    narrator = jsondata['narrator']

    create_query = '''CREATE TABLE IF NOT EXISTS AUDIOBOOK
                   (ID INT PRIMARY KEY NOT NULL,
                   NAME TEXT(100),
                   DURATION LONG,
                   UPLOADEDTIME DATETIME,
                   AUTHOR TEXT(100),
                   NARRATOR TEXT(100)
                   )'''

    db.execute(create_query)
    insert_query = '''INSERT OR REPLACE INTO AUDIOBOOK(id,name,duration,uploadedtime,AUTHOR,NARRATOR) VALUES(?,?,?,?,?,?)'''
    db.execute(insert_query, [id, name,duration,uploadedTime,author,narrator])
    conn.commit()
    db.execute('''select * from AUDIOBOOK''')
    values = db.fetchall()
    print("val@", values)
    return "Action is successful,200 OK"


def get_audiofile(conn, filetype, songId):
    db = conn.cursor()
    if songId is None:
        select_query = f'''select * from {filetype}'''
        db.execute(select_query)
        values = db.fetchall()
        return json.dumps(values)
    else:

        select_query = f'''select * from {filetype} where id={songId}'''
        db.execute(select_query)
        values = db.fetchall()
        return json.dumps(values)


def remove_audiofile(conn, filetype, songId):
    try:
        db = conn.cursor()
        db.execute(f'''select ID from {filetype} where id={songId}''')
        result = db.fetchall()
        print(result)
        delete_query = f'''delete from {filetype} where id={songId}'''
        db.execute(delete_query)
        conn.commit
        print("deleted from db")
    except Error as e:
        print("error!!", e)


def update_song(conn, jsondata):
    try:
        db = conn.cursor()
        print("entered update_song method")
        print("json meta", jsondata)
        # results=[]
        # for values in jsondata.items:
        #     results.append(values)

        id = jsondata['ID']
        name = jsondata['name']
        duration = jsondata['duration']
        uploadedTime = jsondata['uploadedTime']

        create_query = '''CREATE TABLE IF NOT EXISTS SONG
                           (
                           ID INT PRIMARY KEY  not null,
                           NAME TEXT(100),
                           DURATION LONG,
                           UPLOADEDTIME DATETIME
                           )'''


        db.execute(create_query)
        insert_query='''INSERT OR REPLACE INTO SONG(id,name,duration,uploadedtime) VALUES(?,?,?,?)'''
        db.execute(insert_query, [id,name,duration,uploadedTime])
        conn.commit()
        db.execute('''select * from songs''')
        values = db.fetchall()
        print("val@",values)
        return "Action is successful,200 OK"
    except Error as e:
        print(e)


def update_podcast(conn,jsondata):

    db = conn.cursor()
    print("entered update_podcast method")
    print("json meta", jsondata)
    id = jsondata['ID']
    name = jsondata['name']
    duration = jsondata['duration']
    uploadedTime = jsondata['uploadedTime']
    host = jsondata['host']
    participantsList = jsondata['participants']
    participants=""
    for i in participantsList:
        participants = participants + "," + i

    create_query = '''CREATE TABLE IF NOT EXISTS PODCAST
                   (
                   ID INT PRIMARY KEY NOT NULL,
                   NAME TEXT(100),
                   DURATION LONG,
                   UPLOADEDTIME DATETIME,
                   HOST TEXT(100),
                   PARTICIPANTS TEXT(1000)
                   )'''

    db.execute(create_query)
    insert_query='''INSERT OR REPLACE INTO PODCAST(id,name,duration,uploadedtime, host, participants) VALUES(?,?,?,?,?,?)'''
    db.execute(insert_query, [id, name, duration, uploadedTime, host, participants])
    conn.commit()
    db.execute('''select * from PODCAST''')
    values = db.fetchall()
    print("val@",values)
    return "Action is successful,200 OK"


def update_audiobook(conn, jsondata):

    db = conn.cursor()
    print("entered update_audiobook method")
    print("json meta", jsondata)
    id = jsondata['ID']
    name = jsondata['name']
    duration = jsondata['duration']
    uploadedTime = jsondata['uploadedTime']
    author = jsondata['author']
    narrator = jsondata['narrator']

    create_query = '''CREATE TABLE IF NOT EXISTS AUDIOBOOK
                   (ID INT PRIMARY KEY NOT NULL,
                   NAME TEXT(100),
                   DURATION LONG,
                   UPLOADEDTIME DATETIME,
                   AUTHOR TEXT(100),
                   NARRATOR TEXT(100)
                   )'''

    db.execute(create_query)
    insert_query = '''INSERT OR REPLACE INTO AUDIOBOOK(id,name,duration,uploadedtime,AUTHOR,NARRATOR) VALUES(?,?,?,?,?,?)'''
    db.execute(insert_query, [id, name,duration,uploadedTime,author,narrator])
    conn.commit()
    db.execute('''select * from AUDIOBOOK''')
    values = db.fetchall()
    print("val@", values)
    return "Action is successful,200 OK"










