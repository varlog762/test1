'''Gregoty Pereverzev 02.12.2019'''
from flask import Flask
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() ->str:
    return 'Hello world from Flusk'



@app.route('/search4')
def do_search() ->str:
    set0 = search4letters('life, the universe, and everything!', 'eiru,!')

    return str(set0)

app.run()