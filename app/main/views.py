from flask import render_template
from . import main
from flask_login import login_required

@main.route('/')
def home():
    '''Home route'''
    return render_template('index.html')


@main.route('/comment')
@login_required
def comment():
    pass
