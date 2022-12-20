import unittest

import logic


class TestLogic(unittest.TestCase):
    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        board1 = [
            ['O', None, 'O'],
            [None, 'O', None],
            [None, 'O', 'O'],
        ]
        board2 = [
            ['O', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        self.assertEqual(logic.get_winner(board1), 'O')
        self.assertEqual(logic.get_winner(board2), None)

    # TODO: Test all fuctions from logic.py!

    def test_other_player(self):
        player = '1'
        self.assertEqual(logic.other_player(player), '0')
        player2 = '0'
        self.assertEqual(logic.other_player(player2), '1')

    def test_make_empty_board(self):
        empty_board = [    
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
        self.assertEqual(logic.make_empty_board(), empty_board)

if __name__ == '__main__':
    unittest.main()