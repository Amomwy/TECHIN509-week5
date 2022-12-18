import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        """
        Test if get_winner() function works as expected.
        """
       
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def test_empty_board(self):
        """
        Test if empty_board() function works as expected.
        """
        correct_board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

        self.assertEqual(logic.empty_board(), correct_board)

    def test_other_player(self):
        """
        Test if other_player() function works as expected.
        """
        
        self.assertEqual(logic.other_player("X"), "O")
        self.assertEqual(logic.other_player("O"), "X")


if __name__ == '__main__':
    unittest.main()