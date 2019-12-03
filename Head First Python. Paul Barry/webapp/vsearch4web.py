'''Gregoty Pereverzev 02.12.2019'''
from flask import Flask, render_template
from vsearch import search4letters


app = Flask(__name__)

@app.route('/')
def hello() ->str:
    return 'Hello world from Flask'



@app.route('/search4')
def do_search() ->str:
    set0 = search4letters('life, the universe, and everything!', 'eiru,!')

    return str(set0)

@app.route('/entry', methods = ['GET', 'POST'])
def entry_page():
    return render_template('entry.html',
                           the_title='Welcome to search4letter on the web!')

app.run()