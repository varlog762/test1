'''Gregoty Pereverzev 02.12.2019'''
from flask import Flask, render_template, request
from vsearch import search4letters


app = Flask(__name__)

@app.route('/')
def hello() ->str:
    return 'Hello world from Flask'



@app.route('/search4', methods = ['POST'])
def do_search() ->str:
    phrase = request.form['phrase']
    letters = request.form['letters']

    return str(search4letters(phrase, letters))

@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letter on the web!')

if __name__ == '__main__':
        app.run(debug = True)

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as vsearch_log:
        print(req + ' ' + res, file=)