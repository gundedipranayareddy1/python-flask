# An object of Flask class is our WSGI application.
import sqlite3

from flask import request

from flask import Flask,Blueprint

#app = Blueprint('AudioFile', __name__)
from AudioFiles.AudioFile import create_song
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
    metadata = request.json['audioFiles']
    filetype = metadata['audioFileType']
    filemeta = metadata['audioFileMetadata']

    print("@@", filetype)
    print("!!", filemeta)
    #with get_db_connection as db:

    conn = sqlite3.connect('database.sqlite')
    if filetype == "song":
        a = create_song(conn, metadata)
        print(a)
        return a
    elif filetype == "podcast":
        return 'podcast'
    elif filetype == "audiobook":
        return 'audiobook'
    else:
        return "unknown filetype"


@app.route('/update/<audioFileType>/<audioFileID>', methods=['GET'])
def update_audiofile(audioFileType,audioFileID):
    return 'updated'


@app.route('/read/<audioFileType>/<audioFileID>', methods=['GET'])
def play_audiofile(audioFileType,audioFileID):
    return 'read'

@app.route('/delete/<audioFileType>/<audioFileID>', methods=['GET'])
def delete_audiofile(audioFileType,audioFileID):
    return 'deleted'


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)
