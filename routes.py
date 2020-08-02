from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html', current_title='Custom Title')


@app.route('/about')
def about():
    return render_template('about.html')
