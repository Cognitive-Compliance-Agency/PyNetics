import unittest

from pynetics.math import Vector2


class Vector2Tests(unittest.TestCase):

    def test_stores_x_and_y(self):
        x = 2
        y = 3
        vector = Vector2(x, y)

        self.assertEqual(vector.x, x)
        self.assertEqual(vector.y, y)

if __name__ == "__main__":
    unittest.main()