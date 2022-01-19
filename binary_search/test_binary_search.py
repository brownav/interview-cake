from iterative_binary_search import binary_search
import unittest

class TestBinarySearch(unittest.TestCase):

    def test_target_found(self):
        actual = binary_search(3, [0, 1, 2, 3, 4,])

        self.assertEqual(actual, 3)


    def test_target_not_found_low(self):
        actual = binary_search(-1, [0, 1, 2, 3, 4])

        self.assertEqual(actual, -1)


    def test_target_not_found_high(self):
        actual = binary_search(6, [0, 1, 2, 3, 4])

        self.assertEqual(actual, -1)


    def test_target_found_edge(self):
        actual = binary_search(0, [0, 1, 2, 3, 4])

        self.assertEqual(actual, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
