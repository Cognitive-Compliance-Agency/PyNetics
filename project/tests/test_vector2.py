import unittest

from pynetics.math import Vector2


class Vector2Tests(unittest.TestCase):

    def test_stores_x_and_y(self):
        vector = Vector2 (x=2, y=3)

        self.assertEqual(vector.x, 2)
        self.assertEqual(vector.y, 3)

if __name__ == "__main__":
    unittest.main()