from app import app
from flask import render_template
import forms


@app.route('/')
def index():
    return render_template('index.html', current_title='Custom Title')


@app.route('/about', methods=['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print("Submited title", form.title.data)
        return render_template('about.html', form=form, title=form.title.data)
    return render_template('about.html', form=form)
