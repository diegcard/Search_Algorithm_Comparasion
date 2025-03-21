import unittest
from search import algorithms
from search.data_generator import get_random_sorted_list

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1, 2, 3, 4], 3, 2),
            ([1], 1, 0),
            ([1, 2, 3], 5, None),
            ([1, 1, 1], 1, 0),
            ([1, 2, 3, 4, 5], 1, 0),
            ([list(range(10000)), 9999, 9999]),
            ([1, 2, 3, 4, 5], 5, 4),
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

    def test_ternary_search(self):
        for arr, target, expected in self.test_cases:
            result = algorithms.ternary_search(arr.copy(), target)
            self.assertEqual(result, expected)