from app import app                 # from app.py, import the app inistance, where app instance is Flask(__name__)
from flask import render_template
import forms                        # This is forms.py specifically

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', current_title="Jesse's Portfolio")    

@app.route('/contact', methods=['GET', 'POST'])
def about():
    form = forms.ContactMeForm()
    if form.validate_on_submit():
        # Store message
        pass
    return render_template('contact.html', form=form)