from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

# Extends the FlaskForm Class to create a custom form
class ContactMeForm(FlaskForm): 
    name = StringField('Name', validators=[DataRequired()])
    company = StringField('Company')
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = StringField('Message', validators=[DataRequired()], render_kw={'style':'height:40ch'})
    submit = SubmitField('Submit')