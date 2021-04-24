from flask import render_template,redirect,url_for, flash,request
from . import main
from flask_login import login_required
from .forms import CategoryForm,PitchForm
from ..models import Category,Pitch
from .. import db

@main.route('/')
def home():
    '''Home route'''
    return render_template('index.html')


@main.route('/comment')
@login_required
def comment():
    pass

@main.route('/addPitchCategory', methods = ["GET","POST"])
@login_required
def addpitchcategory():
    form = CategoryForm()
    if form.validate_on_submit():
        if Category.query.filter_by(category=form.category.data).first() is None:
            category = Category(category=form.category.data)
            db.session.add(category)
            db.session.commit()

            form.category.data = '' #clear form
            flash('Category added successfully','success')
        else:
            form.category.data = '' #clear form
            flash('Category exists, pick a new one','danger')
        

    return render_template('categoryForm.html', category_form=form)


@main.route('/addPitch', methods = ["GET","POST"])
@login_required
def addpitch():
    form = PitchForm()

    form.category.choices = Category.selectFieldChoices() #get categories list of tuples for select input
    selectTop = ('','- select -')  
    form.category.choices.insert(0,selectTop) #prepend '- select- ' to start at top of the select input

    return render_template('pitchForm.html', pitch_form=form)