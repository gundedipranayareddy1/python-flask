from flask import json


def create_song(conn, jsondata):

    db = conn.cursor()
    print("entered create_song method")
    #jsonmeta = jsondata['audioFileMetadata']
    print("json meta", jsondata)
    # results=[]
    # for values in jsondata.items:
    #     results.append(values)

    id=jsondata['ID']
    name=jsondata['name']
    duration=jsondata['duration']
    uploadedTime=jsondata['uploadedTime']

    create_query = '''CREATE TABLE IF NOT EXISTS SONGS
                   (
                   ID INT PRIMARY KEY  not null,
                   NAME TEXT(100),
                   DURATION LONG,
                   UPLOADEDTIME DATETIME
                   )'''

   #insert_query = "INSERT INTO SONGS VALUES(jsondata[audioFileType'],jsonmeta['ID'],jsonmeta['name'],jsonmeta['duration'],jsonmeta['uploadedTime'])"
   # insert_query = '''INSERT INTO SONGS VALUES(4,"hosanaa",2000,"23:23:12")'''

    db.execute(create_query)
    #connection.commit()
    #db.execute(insert_query)
    db.execute("INSERT OR REPLACE INTO SONGS(id,name,duration,uploadedtime) VALUES(?,?,?,?)", [id,name,duration,uploadedTime])
    conn.commit()
    db.execute('''select * from songs''')
    values = db.fetchall()
    print("val@",values)
    #return "Action is successful,200 OK"
    return json.dumps(values)



def create_podcast(conn,jsondata):

    db = conn.cursor()
    print("entered create_song method")
    #jsonmeta = jsondata['audioFileMetadata']
    print("json meta", jsondata)
    id=jsondata['ID']
    name=jsondata['name']
    duration=jsondata['duration']
    uploadedTime=jsondata['uploadedTime']
    host=jsondata['host']
    participants=jsondata['participants']



    create_query = "CREATE TABLE PODCASTS" \
                   "(ID INT PRIMARY KEY NOT NULL," \
                   "NAME TEXT(100)," \
                   "DURATION LONG," \
                   "UPLOADEDTIME DATETIME," \
                   "HOST TEXT(100)," \
                   "PARTICIPANTS TEXT(100)," \
                   ")"


    #insert_query = "INSERT INTO SONGS VALUES(jsondata[audioFileType'],jsonmeta['ID'],jsonmeta['name'],jsonmeta['duration'],jsonmeta['uploadedTime'])"
    # insert_query = '''INSERT INTO SONGS VALUES(4,"hosanaa",2000,"23:23:12")'''

    db.execute(create_query)
    #connection.commit()
    #db.execute(insert_query)
    db.execute("INSERT OR REPLACE INTO PODCASTS(id,name,duration,uploadedtime) VALUES(?,?,?,?,?,?)", [id,name,duration,uploadedTime,host,participants])
    conn.commit()
    db.execute('''select * from songs''')
    values = db.fetchall()
    print("val@",values)
    #return "Action is successful,200 OK"
    return json.dumps(values)


def create_audiobook(conn,jsondata):


    db = conn.cursor()
    print("entered create_song method")
    #jsonmeta = jsondata['audioFileMetadata']
    print("json meta", jsondata)
    id=jsondata['ID']
    name=jsondata['name']
    print("%",name)
    duration=jsondata['duration']
    uploadedTime=jsondata['uploadedTime']
    author=jsondata['author']
    narrator=jsondata['narrator']




    create_query = "CREATE TABLE AUDIOBOOKS" \
                   "(ID INT PRIMARY KEY NOT NULL," \
                   "NAME TEXT(100)," \
                   "DURATION LONG," \
                   "UPLOADEDTIME DATETIME," \
                   "AUTHOR TEXT(100)," \
                   "NARRATOR TEXT(100)," \
                   ")"

    #insert_query = "INSERT INTO SONGS VALUES(jsondata[audioFileType'],jsonmeta['ID'],jsonmeta['name'],jsonmeta['duration'],jsonmeta['uploadedTime'])"
    # insert_query = '''INSERT INTO SONGS VALUES(4,"hosanaa",2000,"23:23:12")'''

    db.execute(create_query)
    #connection.commit()
    #db.execute(insert_query)
    db.execute("INSERT OR REPLACE INTO AUDIOBOOKS(id,name,duration,uploadedtime) VALUES(?,?,?,?,?,?)", [id,name,duration,uploadedTime,author,narrator])
    conn.commit()
    db.execute('''select * from songs''')
    values = db.fetchall()
    print("val@",values)
    #return "Action is successful,200 OK"
    return json.dumps(values)
