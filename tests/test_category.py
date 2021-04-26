import unittest
from app.models import Pitch,User,Category
from app import db

class TestCategoryModel(unittest.TestCase):
    '''Test Model Category'''

    def setUp(self):
        self.category = Category(category='Pick-Up Line')
        db.session.add(self.category)
        db.session.commit()

    def tearDown(self):
        db.session.delete(self.category)
        db.session.commit()

    def test_selectFieldChoices(self):
       # check whether the fxn is giving list of tuples for select field in category form e.g [(3, 'Pitch Category')]
        self.assertEqual( Category.selectFieldChoices(),[(self.category.id ,'Pick-Up Line')])