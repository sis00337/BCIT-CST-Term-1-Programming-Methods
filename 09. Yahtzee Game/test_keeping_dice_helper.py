"""
COMP 1510
09. Yahtzee Game - Yahtzee
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : Delivery_KiKi
"""


import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import select_dice_to_keep_helper


class TestSelectDiceToKeep(TestCase):

    def test_select_dice_to_keep_helper_5_current_dice_right_1_input(self):
        determinant = True
        player_dic = [[1, 1, 2, 3, 3], []]
        user_choice = [3]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    def test_select_dice_to_keep_helper_5_current_dice_right_2_input(self):
        determinant = True
        player_dic = [[1, 1, 2, 3, 3], []]
        user_choice = [3, 3]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    def test_select_dice_to_keep_helper_5_current_dice_right_3_input(self):
        determinant = True
        player_dic = [[1, 1, 2, 3, 3], []]
        user_choice = [1, 1, 2]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    def test_select_dice_to_keep_helper_5_current_dice_right_4_input(self):
        determinant = True
        player_dic = [[1, 1, 2, 3, 3], []]
        user_choice = [1, 1, 2, 3]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    def test_select_dice_to_keep_helper_5_current_dice_right_5_input(self):
        determinant = True
        player_dic = [[1, 1, 2, 3, 3], []]
        user_choice = [1, 1, 2, 3, 3]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    def test_select_dice_to_keep_helper_5_current_dice_right_5_input_reverse(self):
        determinant = True
        player_dic = [[1, 1, 2, 3, 3], []]
        user_choice = [3, 3, 2, 1, 1]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_dice_to_keep_helper_5_current_dice_wrong_input_not_in_current_dice(self, mock_output):
        determinant = True
        player_dic = [[1, 1, 2, 3, 3], []]
        user_choice = [4, 4]
        expected_return = True
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_dice_to_keep_helper_5_current_dice_wrong_input_different_number(self, mock_output):
        determinant = True
        player_dic = [[1, 1, 2, 3, 3], []]
        user_choice = [1, 1, 1]
        expected_return = True
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_dice_to_keep_helper_5_current_dice_wrong_input_longer_than_current_dice(self, mock_output):
        determinant = True
        player_dic = [[1, 1, 2, 3, 3], []]
        user_choice = [1, 1, 2, 3, 3, 3]
        expected_return = True
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_select_dice_to_keep_helper_4_current_dice_right_1_input(self):
        determinant = True
        player_dic = [[1, 1, 2, 3], [3]]
        user_choice = [3]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    def test_select_dice_to_keep_helper_4_current_dice_right_2_input(self):
        determinant = True
        player_dic = [[1, 1, 2, 3], [3]]
        user_choice = [1, 1]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    def test_select_dice_to_keep_helper_4_current_dice_right_3_input(self):
        determinant = True
        player_dic = [[1, 1, 2, 3], [3]]
        user_choice = [1, 1, 2]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    def test_select_dice_to_keep_helper_4_current_dice_right_4_input(self):
        determinant = True
        player_dic = [[1, 1, 2, 3], [3]]
        user_choice = [1, 1, 2, 3]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    def test_select_dice_to_keep_helper_4_current_dice_right_4_input_reverse(self):
        determinant = True
        player_dic = [[1, 1, 2, 3], [3]]
        user_choice = [3, 2, 1, 1]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_dice_to_keep_helper_4_current_dice_wrong_input_not_in_current_dice(self, mock_output):
        determinant = True
        player_dic = [[1, 1, 2, 3], [3]]
        user_choice = [4, 4]
        expected_return = True
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_dice_to_keep_helper_4_current_dice_wrong_input_different_number(self, mock_output):
        determinant = True
        player_dic = [[1, 1, 2, 3], [3]]
        user_choice = [1, 1, 1]
        expected_return = True
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_dice_to_keep_helper_4_current_dice_wrong_input_longer_than_current_dice(self, mock_output):
        determinant = True
        player_dic = [[1, 1, 2, 3], [3]]
        user_choice = [1, 1, 2, 3, 3]
        expected_return = True
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_select_dice_to_keep_helper_3_current_dice_right_1_input(self):
        determinant = True
        player_dic = [[1, 1, 2], [3, 3]]
        user_choice = [2]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    def test_select_dice_to_keep_helper_3_current_dice_right_2_input(self):
        determinant = True
        player_dic = [[1, 1, 2], [3, 3]]
        user_choice = [1, 1]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    def test_select_dice_to_keep_helper_3_current_dice_right_3_input(self):
        determinant = True
        player_dic = [[1, 1, 2], [3, 3]]
        user_choice = [1, 1, 2]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    def test_select_dice_to_keep_helper_3_current_dice_right_3_input_reverse(self):
        determinant = True
        player_dic = [[1, 1, 2], [3, 3]]
        user_choice = [2, 1, 1]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_dice_to_keep_helper_3_current_dice_wrong_input_not_in_current_dice(self, mock_output):
        determinant = True
        player_dic = [[1, 1, 2], [3, 3]]
        user_choice = [3, 4]
        expected_return = True
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_dice_to_keep_helper_3_current_dice_wrong_input_different_number(self, mock_output):
        determinant = True
        player_dic = [[1, 1, 2], [3, 3]]
        user_choice = [1, 1, 1]
        expected_return = True
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_dice_to_keep_helper_3_current_dice_wrong_input_longer_than_current_dice(self, mock_output):
        determinant = True
        player_dic = [[1, 1, 2], [3, 3]]
        user_choice = [1, 1, 2, 3]
        expected_return = True
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_select_dice_to_keep_helper_2_current_dice_right_1_input(self):
        determinant = True
        player_dic = [[1, 1], [3, 3, 3]]
        user_choice = [1]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    def test_select_dice_to_keep_helper_2_current_dice_right_2_input(self):
        determinant = True
        player_dic = [[1, 2], [3, 3, 3]]
        user_choice = [1, 2]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    def test_select_dice_to_keep_helper_2_current_dice_right_2_input_reverse(self):
        determinant = True
        player_dic = [[1, 2], [3, 3, 3]]
        user_choice = [2, 1]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_dice_to_keep_helper_2_current_dice_wrong_input_not_in_current_dice(self, mock_output):
        determinant = True
        player_dic = [[1, 1], [3, 3, 3]]
        user_choice = [3, 4]
        expected_return = True
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_dice_to_keep_helper_2_current_dice_wrong_input_different_number(self, mock_output):
        determinant = True
        player_dic = [[1, 2], [3, 3, 3]]
        user_choice = [2, 2]
        expected_return = True
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_dice_to_keep_helper_2_current_dice_wrong_input_longer_than_current_dice(self, mock_output):
        determinant = True
        player_dic = [[1, 1], [3, 3, 3]]
        user_choice = [1, 1, 2]
        expected_return = True
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    def test_select_dice_to_keep_helper_1_current_dice_right_1_input(self):
        determinant = True
        player_dic = [[6], [3, 3, 3, 3]]
        user_choice = [6]
        expected_return = False
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_dice_to_keep_helper_1_current_dice_wrong_input_not_in_current_dice(self, mock_output):
        determinant = True
        player_dic = [[6], [3, 3, 3, 3]]
        user_choice = [5]
        expected_return = True
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_dice_to_keep_helper_1_current_dice_wrong_input_different_number(self, mock_output):
        determinant = True
        player_dic = [[6], [3, 3, 3, 3]]
        user_choice = [6, 6]
        expected_return = True
        actual_return = select_dice_to_keep_helper(determinant, player_dic, user_choice)
        expected_print = 'You entered the wrong input. Please try again.\n'
        actual_print = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_print, actual_print)
