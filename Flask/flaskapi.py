# An object of Flask class is our WSGI application.
import sqlite3

from flask import request
from flask import Flask
from AudioFiles.AudioFile import create_song, create_podcast, create_audiobook, get_audiofile, remove_audiofile
from Database.database import get_db_connection

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/create', methods=['GET'])
def create_audiofile():
    #metadata = request.json['audioFiles']
    metadata = request.json
    print("$", metadata)
    filetype = metadata['audioFileType']
    filemeta = metadata['audioFileMetadata']

    print("@@", filetype)
    print("!!", filemeta)
    with get_db_connection() as conn:
        if filetype == "song":
            song = create_song(conn, filemeta)
            print(song)
            return song
        elif filetype == "podcast":
            podcast = create_podcast(conn, filemeta)
            print(podcast)
            return podcast
        elif filetype == "audiobook":
            audiobook = create_audiobook(conn, filemeta)
            print(audiobook)
            return audiobook
        else:
            return bad_request


@app.route('/update/<string:audioFileType>/<int:audioFileID>', methods=['GET'])
def update_audiofile(audioFileType,audioFileID):
    metadata = request.json
    print("$", metadata)
    filetype = metadata['audioFileType']
    filemeta = metadata['audioFileMetadata']

    print("@@", filetype)
    print("!!", filemeta)
    with get_db_connection() as conn:
        if filetype == "song":
            song = create_song(conn, filemeta)
            print(song)
            return song
        elif filetype == "podcast":
            podcast = create_podcast(conn, filemeta)
            print(podcast)
            return podcast
        elif filetype == "audiobook":
            audiobook = create_audiobook(conn, filemeta)
            print(audiobook)
            return audiobook
        else:
            return bad_request()



@app.route('/read/<audioFileType>', methods=['GET'])
@app.route('/read/<audioFileType>/<audioFileID>', methods=['GET'])
def read_audiofile(audioFileType, audioFileID=None):
    with get_db_connection() as conn:
        try:
            if audioFileType in ("song", "podcast", "audiobook"):
                audiofile = get_audiofile(conn, audioFileType, audioFileID)
                print(audiofile)
                if audiofile == "[]":
                    return bad_request()
                else:
                    return audiofile
            else:
                return bad_request()
        except sqlite3.Error as e:
            error_message




@app.route('/delete/<string:audioFileType>/<int:audioFileID>', methods=['GET'])
def delete_audiofile(audioFileType,audioFileID):
    with get_db_connection() as conn:
        try:
            if audioFileType in ("song", "podcast", "audiobook"):
                audioFile = remove_audiofile(conn, audioFileType, audioFileID)
                print(audioFile)
                return "Action is successful: 200 OK"
            else:
                return bad_request
        except sqlite3.Error:
            return error_message



@app.errorhandler(500)
def error_message():
    return "<h1>505</h1><p>500 internal server error</p>", 500

# @app.errorhandler(404)
# def page_not_found():
#     return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.errorhandler(400)
def bad_request():
    return "<h1>400</h1><p>The request is invalid: 400 bad request</p>", 400

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)
