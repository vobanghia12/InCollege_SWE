import unittest
from unittest.mock import patch
import menuFunctions
import accountFunctions
import io


#testing friend requests
class TestSendConnectionRequest(unittest.TestCase):

    def setUp(self):
        # Create a sample student account
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

    def tearDown(self):
        # Clean up the sample student account
        accountFunctions.ALL_STUDENT_ACCOUNTS.clear()

    @patch('builtins.input', side_effect=['2', '1', 'User', 'yes', '4', '6'])
    def test_send_connection_request_lastname(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            menuFunctions.main_menu('Test', 'User')
            output = mock_stdout.getvalue()

        # Check if search results are displayed
        self.assertIn("Found: Test User", output)

        # Check if the connection request is sent
        self.assertIn("Connection request sent to Test User", output)


    @patch('builtins.input', side_effect=['2', '2', 'Sample University', 'yes', '4', '6'])
    def test_send_connection_request_university(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            menuFunctions.main_menu('Test', 'User')
            output = mock_stdout.getvalue()

        # Check if search results are displayed
        self.assertIn("Found: Test User", output)

        # Check if the connection request is sent
        self.assertIn("Connection request sent to Test User", output)


    @patch('builtins.input', side_effect=['2', '3', 'Sample Major', 'yes', '4', '6'])
    def test_send_connection_request_major(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            menuFunctions.main_menu('Test', 'User')
            output = mock_stdout.getvalue()

        # Check if search results are displayed
        self.assertIn("Found: Test User", output)

        # Check if the connection request is sent
        self.assertIn("Connection request sent to Test User", output)


if __name__ == '__main__':
    unittest.main()
