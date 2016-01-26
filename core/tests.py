import unittest
import os
from app import app, db
from parser import Parser

dirname = os.path.abspath(os.path.dirname(__file__))
path_to_new_file = os.path.join(os.path.join(dirname, 'templates'), 'tests.html')

class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dirname, 'test_app.db')
        self.app = app.test_client()
        db.create_all()
        if not os.path.exists(path_to_new_file):
            open(path_to_new_file, 'w')

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_parser(self):
        with open(path_to_new_file, 'r+') as new_file:
            new_file.write("for i in range(100): print i")
            p = Parser('tests.html')
            parse = p.parse_file()
            self.assertEqual(parse, [('for', 'keyword'), ('in', 'keyword'), ('range', 'built_in_function'), ('print', 'keyword')
            ])


if __name__ == '__main__':
    unittest.main()
