import email_validator
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, ValidationError, TextAreaField,SelectField #,BooleanField
from wtforms.validators import DataRequired,Email ,Length
from ..models import User,Pitch,Category

class CategoryForm(FlaskForm):
    '''Class to generate category form'''

    category = StringField('Name of Pitch Category',validators=[DataRequired()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    '''Class to generate pitch form'''

    pitch = TextAreaField('Pitch', validators=[DataRequired()])
    category = SelectField('Programming Language',validators=[DataRequired()])
    submit = SubmitField('Submit')

   