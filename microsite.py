import flask
from flask import Flask, render_template, \
    url_for, request, flash, redirect,session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uhuvnp213i7czoo82'

menu = [{'name': 'Установка', 'url': 'install-Flask'},
        {'name': 'First Application', 'url': 'first-app'},
        {'name': 'Feedback', 'url': 'feedback'},
        {'name': 'About', 'url': 'about'}]


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='SASAI LALKA', menu=menu)


@app.route('/profile/<username>')
def profile(username):
    return f'User: {username}'


@app.route('/feedback', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Message was sent', category='success')
        else:
            flash('Oops! Something is going wrong...', category='error')
        print(request.form['username'])
    return render_template('contact.html', title='Feedback', menu=menu)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'selfedu' and request.form['psw'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title='Authorization', menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/page404.html', title='Страница не найдена', menu=menu), 404


'''
with app.test_request_context():
    print(url_for('index'))
    print(url_for('about'))
    print(url_for('profile', username='123213'))
'''

if __name__ == '__main__':
    app.run(debug=True)
