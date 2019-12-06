'''Gregoty Pereverzev 02.12.2019'''
from flask import Flask, render_template, request
from vsearch import search4letters


app = Flask(__name__)



@app.route('/')
def hello() ->str:
    return 'Hello world from Flask'



def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as vsearch_log:
        print(req + ' ' + res, file=vsearch_log)



@app.route('/search4', methods = ['POST'])
def do_search() ->str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your result: '
    results = str(search4letters(phrase, letters))
    log_request(str(phrase + ' ' + letters), str(search4letters(phrase, letters)))

    return render_template('result.html',
                           the_title = title,
                           the_phrase = phrase,
                           the_letters = letters,
                           the_results = results)

@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letter on the web!')

if __name__ == '__main__':
        app.run(debug = True)

