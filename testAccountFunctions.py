import unittest
from accountFunctions import createAccount, checkUser, checkUniqueUsername, checkValidPassword, checkForName
import accountFunctions

class TestAccountFunctions(unittest.TestCase):
    def test_createAccount(self):
        # Test with valid input
        self.assertEqual(createAccount('John', 'Doe', 'johndoe', 'password123'), ('John', 'Doe'))

        # Test with invalid password
        self.assertRaises(ValueError, createAccount, 'Jane', 'Doe', 'janedoe', 'pass')

        # Test with non-unique username
        self.assertRaises(ValueError, createAccount, 'Bob', 'Smith', 'johndoe', 'password123')

    def test_checkUser(self):
        # Test with valid username and password
        self.assertTrue(checkUser('johndoe', 'password123'))

        # Test with invalid username and password
        self.assertFalse(checkUser('janedoe', 'password123'))

    def test_checkUniqueUsername(self):
        # Test with unique username
        self.assertTrue(checkUniqueUsername('janedoe'))

        # Test with non-unique username
        self.assertFalse(checkUniqueUsername('johndoe'))

    def test_checkValidPassword(self):
        # Test with valid password
        self.assertTrue(checkValidPassword('password123'))

        # Test with invalid password
        self.assertFalse(checkValidPassword('pass'))

    def test_checkForName(self):
        # Test with existing name
        self.assertTrue(checkForName('John', 'Doe'))

        # Test with non-existing name
        self.assertFalse(checkForName('Jane', 'Doe'))


##############
# testing account creations for 10 accounts
class TestStudentAccounts(unittest.TestCase):

    def test_max_student_accounts(self):
        # Create 10 student accounts
        for i in range(accountFunctions.MAX_STUDENT_ACCOUNTS):
            username = f"user{i}"
            password = "Password123"
            firstName = f"First{i}"
            lastName = f"Last{i}"
            university = "Sample University"
            major = "Sample Major"
            
            accountFunctions.ALL_STUDENT_ACCOUNTS[username] = {
                'password': password,
                'firstName': firstName,
                'lastName': lastName,
                'university': university,
                'major': major,
                'friends': [],
                'Language': 'English',
                'SMS': True,
                'Email': True,
                'Advertising': True
            }
        
        # Try to create one more account, which should exceed the limit
        exceeded_account = accountFunctions.createAccount()
        
        # Check if the maximum accounts limit is enforced
        self.assertEqual(len(accountFunctions.ALL_STUDENT_ACCOUNTS), accountFunctions.MAX_STUDENT_ACCOUNTS)
        self.assertIsNone(exceeded_account, "Exceeded account should be None")



#testing list of friends is empty
class TestStudentFriends(unittest.TestCase):

    def test_empty_friends_list(self):
        # Create a new account
        username = "testuser"
        password = "Password123"
        firstName = "Test"
        lastName = "User"
        university = "Sample University"
        major = "Sample Major"
        
        accountFunctions.ALL_STUDENT_ACCOUNTS[username] = {
            'password': password,
            'firstName': firstName,
            'lastName': lastName,
            'university': university,
            'major': major,
            'friends': [],
            'Language': 'English',
            'SMS': True,
            'Email': True,
            'Advertising': True
        }
        
        # Check if the newly created account has an empty friends list
        self.assertEqual(len(accountFunctions.ALL_STUDENT_ACCOUNTS[username]['friends']), 0)


if __name__ == '__main__':
    unittest.main()
