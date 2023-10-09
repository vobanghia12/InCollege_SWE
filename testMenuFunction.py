import unittest
import main
from unittest.mock import patch
from io import StringIO
from menuFunctions import main_menu, find


class TestMenuFunctions(unittest.TestCase):
    def test_mainMenu(self):
        # Test with valid input
        with patch('builtins.input', side_effect=['1', '6']):
            with patch('sys.stdout', new=StringIO()) as fakeOutput:
                main_menu('John', 'Doe')
                self.assertIn('6. Return to main menu', fakeOutput.getvalue())

        # Test with invalid input
        with patch('builtins.input', side_effect=['7', '6']):
            with patch('sys.stdout', new=StringIO()) as fakeOutput:
                main_menu('John', 'Doe')
                self.assertIn('Invalid input', fakeOutput.getvalue())



    @patch('builtins.input', side_effect=['1', '1', '7', '1', '2', '5'])
    def test_general_submenu(self, mock_input):
        with patch('builtins.print') as mock_print:
            main.display_useful_links()
            mock_print.assert_called_with("We're here to help")
            main.display_useful_links()
            mock_print.assert_called_with("In College: Welcome to In College, the world's largest college student network...")
            main.display_useful_links()
            mock_print.assert_called_with("\nGeneral:")
            main.display_useful_links()
            mock_print.assert_called_with("We're here to help")
            main.display_useful_links()
            mock_print.assert_called_with("In College: Welcome to In College, the world's largest college student network...")
            main.display_useful_links()
            mock_print.assert_called_with("Careers")

    @patch('builtins.input', side_effect=['2', '3', '4', '5'])
    def test_under_construction_options(self, mock_input):
        with patch('builtins.print') as mock_print:
            main.display_useful_links()
            mock_print.assert_called_with("Under construction")
            main.display_useful_links()
            mock_print.assert_called_with("Under construction")
            main.display_useful_links()
            mock_print.assert_called_with("Under construction")
            main.display_useful_links()
            mock_print.assert_called_with("Useful Links:")

    @patch('builtins.input', side_effect=['6', '7', 'invalid', '5'])
    def test_invalid_options(self, mock_input):
        with patch('builtins.print') as mock_print:
            main.display_useful_links()
            mock_print.assert_called_with("Invalid choice.")
            main.display_useful_links()
            mock_print.assert_called_with("Under construction")
            main.display_useful_links()
            mock_print.assert_called_with("Invalid choice.")
            main.display_useful_links()
            mock_print.assert_called_with("Useful Links:")

    @patch('builtins.input', side_effect=['5'])
    def test_return_to_main_menu(self, mock_input):
        with patch('builtins.print') as mock_print:
            with patch('main.main') as mock_main:
                main.display_useful_links()
                mock_main.assert_called_once()

# moving the functions below into the class will break them, please dont move

def input_notLoggedInMenu(prompt):
    if "Select an option with numbers 1-6: " in prompt:
        return "1"
    if "Select an option: " in prompt:
        return "1"
    if "Select a option: " in prompt:
        return "7"
    if "Do you want to go back to the useful links page?: y/n" in prompt:
        return "n"


def input_notLoggedinMenuImportantLinks(prompt):
    if "Select an option with numbers 1-6: " in prompt:
        return "2"
    if "Select an option: " in prompt:
            return "1"
    if "Do you want to go back to the useful important page?: y/n" in prompt:
        return "n"

def input_usefulLinks_choice_1(prompt):
        if "Select an option: " in prompt:
            return "1"
        if "Select a option: " in prompt:
            return "7"
        if "Do you want to go back to the useful links page?: y/n" in prompt:
            return "n"

def input_importantLinks_choice_1(prompt):
    if "Select an option: " in prompt:
        return "1"
    if "Do you want to go back to the useful important page?: y/n" in prompt:
        return "n"


def test_importantLinks(capsys, monkeypatch):
    try:
        monkeypatch.setattr("builtins.input", input_importantLinks_choice_1)
        main.display_important_links()
        captured = capsys.readouterr()
        assert "\nInCollege Important Links:" in captured.out
        assert "1. Copyright Notice" in captured.out
        assert "2. About" in captured.out
        assert "3. Accessibility" in captured.out
        assert "4. User Agreement" in captured.out
        assert "5. Cookie Policy" in captured.out
        assert "6. Copyright Policy" in captured.out
        assert "7. Brand Policy" in captured.out
        assert "8. Return to login screen" in captured.out
    except SystemExit as error:
        assert str(error) == "Goodbye !"


def test_usefulLinks(capsys, monkeypatch):
    try:
        monkeypatch.setattr("builtins.input", input_usefulLinks_choice_1)
        main.display_useful_links()
        captured = capsys.readouterr()
        assert "\nUseful Links:" in captured.out
        assert "1. General" in captured.out
        assert "2. Browse InCollege" in captured.out
        assert "3. Business Solutions" in captured.out
        assert "4. Directories" in captured.out
        assert "5. Return to Main Menu" in captured.out
    except SystemExit as error:
        assert str(error) == "Goodbye !"

def test_notLoggedInUsefulLinks(capsys, monkeypatch):
    try:
        monkeypatch.setattr("builtins.input", input_notLoggedInMenu)
        main.main()
        captured = capsys.readouterr()
        assert "\nUseful Links:" in captured.out
        assert "1. General" in captured.out
        assert "2. Browse InCollege" in captured.out
        assert "3. Business Solutions" in captured.out
        assert "4. Directories" in captured.out
        assert "5. Return to Main Menu" in captured.out
    except SystemExit as error:
        assert str(error) == "Goodbye !"

def test_notLoggedinMenuImportantLinks(capsys, monkeypatch):
    try:
        monkeypatch.setattr("builtins.input", input_notLoggedinMenuImportantLinks)
        main.main()
        captured = capsys.readouterr()
        assert "\nInCollege Important Links:" in captured.out
        assert "1. Copyright Notice" in captured.out
        assert "2. About" in captured.out
        assert "3. Accessibility" in captured.out
        assert "4. User Agreement" in captured.out
        assert "5. Cookie Policy" in captured.out
        assert "6. Copyright Policy" in captured.out
        assert "7. Brand Policy" in captured.out
        assert "8. Return to login screen" in captured.out
    except SystemExit as error:
        assert str(error) == "Goodbye !"


#############
#Testing find
def input_find(prompt):
    if "Select an option: " in prompt:
        return "4"
    if "Select a option: " in prompt:
        return "6"
    

def test_find(capsys, monkeypatch):
    try:
        monkeypatch.setattr("builtins.input", input_find)
        find()
        captured =capsys.readouterr()
        assert "1. Search by last name" in captured.out
        assert "2. Search by university" in captured.out
        assert "3. Search by major" in captured.out
        assert "4. Return to main menu" in captured.out
    except SystemExit as error:
        assert str(error) == "Goodbye !"



if __name__ == '__main__':
    unittest.main()