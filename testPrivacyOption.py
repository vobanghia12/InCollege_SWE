import unittest
from unittest.mock import patch
import main
import accountFunctions
import menuFunctions

class TestPrivacyFunction(unittest.TestCase):

    def setUp(self):
        # Set up any necessary test data or variables
        self.username = "testuser"
        self.password = "testpassword"
        self.fName = "Test"
        self.lName = "User"

    def tearDown(self):
        # Clean up after each test
        pass

    @patch("builtins.input")
    def test_privacy_policy_selection(self, mock_input):
        # Simulate user selecting Privacy Policy option
        mock_input.side_effect = ["3", "2"]  # Select Privacy Policy and then Guest Controls
        main.isLoggedIn = True  # Simulate that the user is logged in
        with patch('menuFunctions.main_menu', return_value='toMain'):
            result = main.main()
        self.assertEqual(result, 'toMain')

    @patch("builtins.input")
    def test_guest_controls_setting(self, mock_input):
        # Simulate user selecting Privacy Policy and then Guest Controls option
        mock_input.side_effect = ["3", "2"]  
        main.isLoggedIn = True
        with patch('menuFunctions.main_menu', return_value='toMain'):
            main.main()

        # Simulate user turning off Email, SMS, and Targeted Advertising
        mock_input.side_effect = ["1", "2", "3"]
        with patch('menuFunctions.main_menu', return_value='toMain'):
            result = main.main()
        
        # Check if the settings are updated in the accountFunctions module
        user_info = accountFunctions.ALL_STUDENT_ACCOUNTS[self.username]
        self.assertFalse(user_info['Email'])
        self.assertFalse(user_info['SMS'])
        self.assertFalse(user_info['Advertising'])

if __name__ == '__main__':
    unittest.main()