import email_validator
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, ValidationError #,BooleanField
from wtforms.validators import Required,Email #,EqualTo
from ..models import User,Pitch,Category

class CategoryForm(FlaskForm):
    '''Class to generate category form'''

    category = StringField('Name of Pitch Category',validators=[Required()])
    submit = SubmitField('Submit')

    # def validate_category(self,data_field):
    #     '''Check if the category is presents, return a boolean'''
    #     if Category.query.filter_by(category=data_field.data).first():
    #         raise ValidationError('Pitch category exists')