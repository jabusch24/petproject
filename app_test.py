import unittest
from app import get_words, enter_difficulty, game_finish
from io import StringIO
from unittest.mock import patch


class TestApp(unittest.TestCase):

    def test_get_words(self):
        res = get_words(5)
        self.assertEqual(len(res[0]), 100)

    def test_enter_difficulty(self):
        user_input = [
            '3'
        ]
        expected_stacks = [
            3
        ]
        with patch('builtins.input', side_effect=user_input):
            stacks = enter_difficulty()
        self.assertEqual(stacks, expected_stacks[0])

    def test_game_finish(self):
        user_input = [
            'n'
        ]
        expected_stacks = [
            False
        ]
        with patch('builtins.input', side_effect=user_input):
            stacks = game_finish()
        self.assertEqual(stacks, expected_stacks[0])


if __name__ == '__main__':
    unittest.main()
