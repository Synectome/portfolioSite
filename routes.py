from app import app, db             # from app.py, import the app inistance, where app instance is Flask(__name__)
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models import Message
import forms                        # This is forms.py specifically

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = forms.ContactMeForm()
    if form.validate_on_submit():
        mesg = Message(name=form.name.data, 
            company=form.company.data, 
            email=form.email.data, 
            message=form.message.data)
        db.session.add(mesg)
        db.session.commit()
        flash('Thank you for contacting me.\nI will be in touch soon.')
        # url_for is taking in a funciton name here
        return redirect(url_for('index'))
    return render_template('index.html', form=form, current_title="Jesse's Portfolio")    

# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     form = forms.ContactMeForm()
#     if form.validate_on_submit():
#         mesg = Message(name=form.name.data, 
#             company=form.company.data, 
#             email=form.email.data, 
#             message=form.message.data)
#         db.session.add(mesg)
#         db.session.commit()
#         flash('Thank you for contacting me.\nI will be in touch soon.')
#         # url_for is taking in a funciton name here
#         return redirect(url_for('index'))
#     return render_template('contact.html', form=form)