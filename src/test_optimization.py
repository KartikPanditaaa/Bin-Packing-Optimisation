import unittest
from optimization import is_valid_placement

class TestOptimization(unittest.TestCase):
    def test_valid_placement(self):
        # Example test case for a valid placement
        area = [[False] * 10 for _ in range(10)]
        self.assertTrue(is_valid_placement(area, 0, 0, 5, 5))

    def test_invalid_placement(self):
        # Example test case for an invalid placement
        area = [[False] * 10 for _ in range(10)]
        area[0][0] = True  # Mark top-left corner as used
        self.assertFalse(is_valid_placement(area, 0, 0, 5, 5))

if __name__ == "__main__":
    unittest.main()
