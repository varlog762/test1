'''Gregoty Pereverzev 02.12.2019'''
from flask import Flask, render_template, request
from vsearch import search4letters


app = Flask(__name__)



@app.route('/')
@app.route('/entry')
def entry_page() ->'html':
    '''Выводит стартовую приветственную таблицу и предлагает
    ввести фразу и перечень букв для поиска.'''
    return render_template('entry.html',
                           the_title='Welcome to search4letter on the web!')



def log_request(req: 'flask_request', res: str) -> None:
    '''Записывает пользовательский запрос и результат работы do_search в лог-файл.'''
    with open('vsearch.log', 'a') as log:
        print(req, res, file=log)



@app.route('/search4', methods = ['POST'])
def do_search() ->'html':
    '''Принимает пользовательский ввод, обрабатывает, вызывает функцию логирования
     и выводит страницу с результами обработки'''
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your result: '
    results = str(search4letters(phrase, letters))
    log_request(phrase + letters, results)
    return render_template('results.html',
                           the_title = title,
                           the_phrase = phrase,
                           the_letters = letters,
                           the_results = results)



@app.route('/viewlog')
def view_the_log() ->str:
    with open('vsearch.log') as log:
        contents = log.read()
    return contents



if __name__ == '__main__':
        app.run(debug = True)