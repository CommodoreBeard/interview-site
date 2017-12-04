from flask import Flask, render_template, request, redirect
from flask_nav import Nav
from flask_nav.elements import *
from flask_bootstrap import Bootstrap

from forms import SearchForm
from items import items

app = Flask(__name__)
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_xxx'
)

Bootstrap(app)

nav = Nav()
@nav.navigation()
def mynavbar():
    return Navbar(
        View('HOME', 'index')
    )
nav.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('search') + '?term={}'.format(form.data['search_term']))
    return render_template('index.html', form=form)

@app.route('/search')
def search():
    term = request.args.get('term')
    if term.lower() != 'iphone':
        return render_template('error.html')
    return render_template('search_results.html', items=items())


if __name__ == '__main__':
    app.run(host='0.0.0.0')