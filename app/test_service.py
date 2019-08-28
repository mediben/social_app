import unittest
from service import add_user, follow_user, profile_user, wall_user, post_user

class TestService(unittest.TestCase):
    
    
    def test_add(self):
        self.assertIsNone(add_user('[user1, add]'))
        self.assertFalse(add_user('user add'))
        self.assertEqual(add_user('[user2, add]'), None)
        self.assertRaises(ValueError, add_user, ['12_23', 'add'])
        
    def test_follow(self):
        self.assertEqual(add_user('[user1, follows, user2]'), None)
        self.assertRaises(IndexError, add_user['user1', 'follows', 'user 2', 'user 3'])
    
    def test_post(self):
        self.assertIsNone(post_user('[user1, Hello World!]'))
        self.assertIsNone(post_user('[user2, Hello user1]'))
    
    def test_profile(self):
        self.assertEqual(profile_user('user 1'), '[Hello World!]')

    def test_wall(self):
        self.assertEqual(profile_user('user 1'), '[Hello World!, Hello user1]')
        
    def test_program(self):
        pass