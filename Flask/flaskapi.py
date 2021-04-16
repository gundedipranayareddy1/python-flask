# An object of Flask class is our WSGI application.
import sqlite3

from flask import request

from flask import Flask,Blueprint

#app = Blueprint('AudioFile', __name__)
from AudioFiles.AudioFile import create_song, create_podcast, create_audiobook
from Database.database import get_db_connection

app = Flask(__name__)

# Flask constructor takes the name of 
# current module (__name__) as argument.


# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


@app.route('/create', methods=['GET'])
def create_audiofile():
    #metadata = request.json['audioFiles']
    metadata = request.json
    print("$",metadata)
    filetype = metadata['audioFileType']
    print("!",filetype)
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
            return 'podcast'
        elif filetype == "audiobook":
            audiobook = create_audiobook(conn, filemeta)
            print(audiobook)
            return 'audiobook'
        else:
            return "unknown filetype"


# @app.route('/update/<audioFileType:String>/<audioFileID:int>', methods=['GET'])
# def update_audiofile(audioFileType,audioFileID):
#     return 'updated'
#
#
# @app.route('/read/<audioFileType:String>/<audioFileID:int>', methods=['GET'])
# def play_audiofile(audioFileType,audioFileID):
#     return 'read'
#
# @app.route('/delete/<audioFileType:String>/<audioFileID:int>', methods=['GET'])
# def delete_audiofile(audioFileType,audioFileID):
#     return 'deleted'


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)
