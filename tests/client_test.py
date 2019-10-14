import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
import unittest
from client import create_presence, process_answer
from basic_things.main_variables import *


class TestClient(unittest.TestCase):
    def test_create_presence(self):
        test = create_presence()
        test[TIME] = 1.1  # Время приравнивается принудильно
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_answer(self):
        self.assertEqual(process_answer({RESPONSE: 200}), '200 : OK')

    def test_400_answer(self):
        self.assertEqual(process_answer({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        self.assertRaises(ValueError, process_answer, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
