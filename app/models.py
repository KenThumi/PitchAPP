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
    pitches = db.relationship('Pitch',backref = 'user',lazy="dynamic")


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
    pitch = db.Column(db.String(255))
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))

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