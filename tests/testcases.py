import json
import unittest
from AudioFiles.AudioFile import create_song, create_podcast, create_audiobook, update_song, update_podcast, \
    update_audiobook, get_audiofile, remove_audiofile
from Database.database import get_db_connection
from Flask.flaskapi import read_audiofile, delete_audiofile


class MyTestCase(unittest.TestCase):
    def test_create_song(self):
        conn = get_db_connection()
        metaData ={
                    "ID": 15,
                    "name": "test_song",
                    "duration": 7000,
                    "uploadedTime": "11:20:30"
                }

        create_song(conn, metaData)
        db=conn.cursor()
        db.execute('''select * from song where ID=15''')
        actual_result= db.fetchall()
        #actual_result = json.dumps(actual_result)
        print("jsondumps",actual_result)


        expected_result = [(15, 'test_song', 7000, '11:20:30')]
        self.assertEqual(actual_result, expected_result)

    def test_create_podcast(self):
        conn = get_db_connection()
        metaData ={
            "ID":32,
            "name":"weekendmasti",
            "duration":5000,
            "uploadedTime":"11:42:42",
            "host":"pranaya",
            "participants":
                [
                    "sita",
                    "gita"
                ]
        }

        create_podcast(conn, metaData)
        db=conn.cursor()
        db.execute('''select * from podcast where ID=32''')
        actual_result= db.fetchall()
        #actual_result = json.dumps(actual_result)
        print("jsondumps",actual_result)

        expected_result = [(32, 'weekendmasti', 5000, '11:42:42', 'pranaya', ',sita,gi')]
        self.assertEqual(actual_result, expected_result)

    def test_create_audiobook(self):
        conn = get_db_connection()
        metaData = {
            "ID":45,
            "name":"weekendmasti",
            "duration":7000,
            "uploadedTime":"9:12:56",
            "author":"aakarsha",
            "narrator":"aakarsha"
            }

        create_audiobook(conn, metaData)
        db=conn.cursor()
        db.execute('''select * from audiobook where ID=45''')
        actual_result= db.fetchall()
        print("jsondumps",actual_result)

        expected_result = [(45, 'weekendmasti', 7000, '9:12:56', 'aakarsha', 'aakarsha')]
        self.assertEqual(actual_result, expected_result)


    def test_update_song(self):
        conn = get_db_connection()
        metaData ={
            "ID": 13,
            "name": "test_update_song",
            "duration": 7000,
            "uploadedTime": "11:20:30"
        }

        update_song(conn, metaData)
        db=conn.cursor()
        db.execute('''select * from song where ID=13''')
        actual_result= db.fetchall()

        expected_result = [(13, 'test_update_song', 7000, '11:20:30')]
        self.assertEqual(actual_result, expected_result)

    def test_update_podcast(self):
        conn = get_db_connection()
        metaData ={
            "ID":33,
            "name":"test_update_podcast",
            "duration":5000,
            "uploadedTime":"11:42:42",
            "host":"aakarsha",
            "participants":
                [
                    "sita",
                    "gita"
                ]
        }

        update_podcast(conn, metaData)
        db=conn.cursor()
        db.execute('''select * from podcast where ID=33''')
        actual_result= db.fetchall()
        print("jsondumps",actual_result)

        expected_result = [(33, 'test_update_podcast', 5000, '11:42:42', 'aakarsha', ',sita,gita')]
        self.assertEqual(actual_result, expected_result)

    def test_update_audiobook(self):
        conn = get_db_connection()
        metaData = {
            "ID":49,
            "name":"test_update_audiobook",
            "duration":7000,
            "uploadedTime":"9:12:56",
            "author":"aakarsha",
            "narrator":"aakarsha"
        }

        update_audiobook(conn, metaData)
        db=conn.cursor()
        db.execute('''select * from audiobook where ID=49''')
        actual_result= db.fetchall()

        expected_result = [(49, 'test_update_audiobook', 7000, '9:12:56', 'aakarsha', 'aakarsha')]
        self.assertEqual(actual_result, expected_result)

    def test_remove_audiofile(self):
        pass

    def test_read_audiofile(self):
        conn = get_db_connection()
        metaData ={
            "ID": 15,
            "name": "test_song",
            "duration": 7000,
            "uploadedTime": "11:20:30"
        }

        create_song(conn, metaData)
        actual_result=get_audiofile(conn,"song",15)
        print("!!!!",actual_result)
        expected_result = json.dumps([[15, 'test_song', 7000, '11:20:30']])
        print("@@@@",expected_result)
        self.assertEqual(actual_result, expected_result)

    def test_remove_audiofile(self):
        conn = get_db_connection()
        metaData ={
            "ID": 16,
            "name": "test_song",
            "duration": 7000,
            "uploadedTime": "11:20:30"
        }

        create_song(conn, metaData)
        actual_result=remove_audiofile(conn,"song",16)
        print("!!!!",actual_result)
        expected_result = None
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
