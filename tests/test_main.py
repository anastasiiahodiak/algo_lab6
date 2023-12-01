import io
import unittest
from unittest.mock import patch

from src.main import build_prefix_table, match, main


class TestStringMatching(unittest.TestCase):

    def test_build_prefix_table(self):
        self.assertEqual(build_prefix_table("abc"), [0, 0, 0])
        self.assertEqual(build_prefix_table("abab"), [0, 0, 1, 2])
        self.assertEqual(build_prefix_table("aaaa"), [0, 1, 2, 3])

    def test_match(self):
        self.assertEqual(match("ababcababcabcabc", "abc"), [2, 7, 10, 13])
        self.assertEqual(match("abababab", "aba"), [0, 2, 4])
        self.assertEqual(match("abcabcabc", "abcd"), [])

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main(self, mock_stdout):
        main()
        expected_result = "[2, 7, 10, 13]\n"
        self.assertEqual(mock_stdout.getvalue(), expected_result)


if __name__ == '__main__':
    unittest.main()