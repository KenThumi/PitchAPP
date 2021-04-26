import unittest
from app.models import Comment,User,Category,Pitch

class CommentModelTest(unittest.TestCase):
    ''' Test if model Comment is working well'''

    def setUp(self):
        '''setup Model instances'''
        self.new_user = User(email='ken@gmail.com', username='Kena', password = 'passward')
        self.category = Category(category='Pick-Up Line')
        self.pitch = Pitch(pitch='Lorem Ipsum',upvote=0,downvote=0,user_id=self.new_user.id,category_id=self.category.id)
        self.comment = Comment(comment='Comment Lorem',pitch_id=self.pitch.id,user_id=self.new_user.id)

    def tearDown(self):
        Comment.query.delete()
        Pitch.query.delete()
        Category.query.delete()
        User.query.delete()


    def test_instance(self):
        self.assertIsInstance(self.comment, Comment)