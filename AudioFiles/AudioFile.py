
def create_song(db, jsondata):

    connection = db.cursor()
    print("entered create_song method")
    jsonmeta = jsondata['audioFileMetadata']
    print("json meta",jsonmeta)

    create_query = '''CREATE TABLE IF NOT EXISTS SONGS
                   (ID INT PRIMARY KEY UNIQUE not null,
                   NAME TEXT(100),
                   DURATION LONG,
                   UPLOADEDTIME DATETIME
                   )'''

   # insert_query = "INSERT INTO SONGS VALUES(jsondata[audioFileType'],jsonmeta['ID'],jsonmeta['name'],jsonmeta['duration'],jsonmeta['uploadedTime'])"
    insert_query = '''INSERT INTO SONGS VALUES(4,"hosanaa",2000,"23:23:12")'''
    connection.execute(create_query)
    #connection.commit()
    connection.execute(insert_query)
    db.commit()
    connection.execute('''select id from songs''')
    values = connection.fetchall()
    return "Action is successful,200 OK"



def create_podcast(db,jsondata):
    create_query = "CREATE TABLE PODCASTS" \
                   "(ID INT PRIMARY KEY NOT NULL," \
                   "NAME TEXT(100)," \
                   "DURATION LONG," \
                   "UPLOADEDTIME DATETIME," \
                   "HOST TEXT(100)," \
                   "PARTICIPANTS TEXT(100)," \
                   ")"


def create_audiobook(db,jsondata):
    create_query = "CREATE TABLE AUDIOBOOKS" \
                   "(ID INT PRIMARY KEY NOT NULL," \
                   "NAME TEXT(100)," \
                   "DURATION LONG," \
                   "UPLOADEDTIME DATETIME," \
                   "AUTHOR TEXT(100)," \
                   "NARRATOR TEXT(100)," \
                   ")"
