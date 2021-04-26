import unittest
from app.models import Pitch,User,Category

class PitchModelTest(unittest.TestCase):
    ''' Test if model Pitch is working well'''

    def setUp(self):
        '''setup Model instances'''
        self.new_user = User(email='ken@gmail.com', username='Kena', password = 'passward')
        self.category = Category(category='Pick-Up Line')
        self.pitch = Pitch(pitch='Lorem Ipsum',upvote=0,downvote=0,user_id=self.new_user.id,category_id=self.category.id)

    def tearDown(self):
        Pitch.query.delete()
        Category.query.delete()
        User.query.delete()


    def test_instance(self):
        self.assertIsInstance(self.pitch, Pitch)