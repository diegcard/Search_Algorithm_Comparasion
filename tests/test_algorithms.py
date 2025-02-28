import unittest
from search import algorithms


class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1, 2, 3, 4], 3, 2),
            ([1], 1, 0),
            ([1, 2, 3], 5, None),
            ([1, 1, 1], 1, 0),
            ([1, 2, 3, 4, 5], 1, 0),
        ]

    def test_linear_search(self):
        for arr, target, expected in self.test_cases:
            result = algorithms.linear_search(arr.copy(), target)
            self.assertEqual(result, expected)

    def test_jump_search(self):
        for arr, target, expected in self.test_cases:
            result = algorithms.jump_search(arr.copy(), target)
            self.assertEqual(result, expected)

    def test_exponential_search(self):
        for arr, target, expected in self.test_cases:
            result = algorithms.exponential_search(arr.copy(), target)
            self.assertEqual(result, expected)