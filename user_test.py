import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def setUp(self):
        '''
        Set up method to run before each test classmethod
        '''
        self.new_user = User("anita","facebook","@anita21","@anita21")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"anita")
        self.assertEqual(self.new_user.acc_type,"facebook")
        self.assertEqual(self.new_user.password,"@anita21")
        self.assertEqual(self.new_user.confirm_password,"@anita21")
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user object list
        '''
        self.new_user.save_user() # saving the new user info
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user_name","twitter","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our contact list
            '''
            self.new_user.save_user()
            test_user = User("Test","user_name","twitter","test@user") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)

    

if __name__ == '__main__':
    unittest.main()