import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
import unittest
from server import message_from_client_func
from basic_things.main_variables import *


class TestServer(unittest.TestCase):
    errors_dict = {
        RESPONSE: 400,
        ERROR: "Bad Request"
    }

    test_passed_dict = {RESPONSE: 200}

    def test_no_action(self):
        self.assertEqual(message_from_client_func({TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.errors_dict)

    def test_wrong_action(self):
        self.assertEqual(message_from_client_func({ACTION: 'Wrong', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}),
                         self.errors_dict)

    def test_no_time(self):
        self.assertEqual(message_from_client_func({ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}),
                         self.errors_dict)

    def test_no_user(self):
        self.assertEqual(message_from_client_func({ACTION: PRESENCE, TIME: '1.1'}), self.errors_dict)

    def test_unknown_user(self):
        self.assertEqual(message_from_client_func({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}),
                         self.errors_dict)

    def test_ok_check(self):
        self.assertEqual(message_from_client_func({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}),
                         self.test_passed_dict)


if __name__ == '__main__':
    unittest.main()
