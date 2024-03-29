from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(UserMixin,db.Model):
    '''Class to handle user'''

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), unique = True)
    email = db.Column(db.String(255), unique = True, index=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String())
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch',backref = 'user',lazy="dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')


    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return f'User {self.username} {self.email}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Pitch(db.Model):
    '''
        Manages a pitch 
        Args: db.Models
    '''

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.Text)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
    comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")

    def __repr__(self):
        return f'Pitch: {self.pitch}'


class Category(db.Model):
    '''
        Manages a category 
        Args: db.Models
    '''

    __tablename__='categories'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'pitch_category',lazy="dynamic")

    @classmethod
    def selectFieldChoices(cls):
        '''creates value,label tuple pairs for select field'''
      
        return [(c.id,c.category) for c in cls.query.all()]


    def __repr__(self):
        return f'Category: {self.category}'


class Comment(db.Model):
    '''
        Manages a comment
        Args: db.Models
    '''

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    

    def __repr__(self):
        return f'Comment: {self.comment}'