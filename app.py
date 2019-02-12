import json
from flask import Flask, abort, request
from board import Board

app = Flask(__name__)
board = Board()


@app.route('/board', methods=['POST'])
def set_board():
    '''HTTP method to set the layout of the board. Accepts a post request with
       a json object consisting of a single value, board, which should be a
       list of list of characters. Some basic verification is done to check if
       a board is sent and that the board doesn't contain any invalid
       characters. Further verification and more descriptive return values
       would be needed in a real app. eg., if the board is square.'''

    data = request.get_json()
    layout = data.get('board')
    if not layout:
        abort(400)
    for line in layout:
        for char in line:
            if (not isinstance(char, basestring) or
               (char != '' and not char.isalpha())):
                abort(400)
    board.set_layout(layout)
    return 'ok'


@app.route('/search/<words>', methods=['GET'])
def search_board(words):
    '''HTTP method to search the board. Accepts a get request which contains a
    list of comma separated words. For example, 'dog,cat,wolf'. Returns a
    json with one value,results, which is a list of found words.'''

    words = words.split(',')
    results = board.find_words(words)
    return json.dumps({'results': results})
