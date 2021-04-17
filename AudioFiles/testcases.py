import unittest

from AudioFiles.AudioFile import create_song
from Database.database import get_db_connection


class MyTestCase(unittest.TestCase):
    def test_something(self):
        conn = get_db_connection
        metaData = {
            "audioFileMetadata":
                {
                    "ID": 1,
                    "name": "priyatamaaa",
                    "duration": 7000,
                    "uploadedTime": "11:20:30"
                }
                }

        with conn.cursor as db:

            create_song(conn, metaData)
            db.execute('''select * from songs''')
            result = db.fetchall
            print(result)
            #self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
