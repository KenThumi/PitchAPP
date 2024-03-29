from flask import render_template,redirect,url_for, flash,request,abort
from . import main
from flask_login import login_required, current_user
from .forms import CategoryForm,PitchForm, CommentForm,UpdateProfile
from ..models import Category,Pitch,Comment,User
from .. import db,photos
from sqlalchemy import desc

@main.route('/')
def home():
    '''Home route'''
    categories = Category.query.all()

    content=[]
    link_categories = []

    for cat in categories:
        pitch = Pitch.query.filter_by(category_id=cat.id).order_by(desc(Pitch.id)).all()
        if len(pitch)>0:                           #take categories that have pitches
            content.append(pitch)
            link_categories.append(cat)

    return render_template('index.html', content=content,  categories = link_categories )


@main.route('/comment/<id>', methods = ["GET","POST"])
@login_required
def comment(id):
    form = CommentForm()

    if form.validate_on_submit():
        if Pitch.query.get(int(id)):
            comment = Comment(comment=form.comment.data,pitch_id=int(id),user_id = current_user.id)
            db.session.add(comment)
            db.session.commit()
            
            flash('Comment added successfully','success')
            return redirect( url_for('main.home'))
        else:
            flash('Subject pitch unretrievable','warning')

    return render_template('commentForm.html', comment_form=form)


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

    if form.validate_on_submit():
        pitch = Pitch(pitch=form.pitch.data,upvote=0,downvote=0,user_id=current_user.id,category_id=form.category.data)  
        db.session.add(pitch)
        db.session.commit()

        form.category.data = '' #clear form
        form.pitch.data = ''

        flash('Pitch added successfully','success')  

    return render_template('pitchForm.html', pitch_form=form)


@main.route('/upvote/<id>')
def upvote(id):
    if Pitch.query.get(int(id)):
        pitch = Pitch.query.get(int(id))
        pitch.upvote +=1
        db.session.add(pitch)
        db.session.commit() 
        flash('Vote submitted successfully','success')
    else:
        flash('Subject pitch unretrievable','warning')

    return redirect( url_for('main.home'))


@main.route('/downvote/<id>')
def downvote(id):
    if Pitch.query.get(int(id)):
        pitch = Pitch.query.get(int(id))
        pitch.downvote +=1
        db.session.add(pitch)
        db.session.commit() 
        flash('Vote submitted successfully','success')
    else:
        flash('Subject pitch unretrievable','warning')
        
    return redirect( url_for('main.home'))


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)



@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))