import unittest
from calc import *


class TestCalc(unittest.TestCase):
    def test_add(self):
        result = add(10, 5)
        self.assertEquals(result, 15)
        self.assertEquals(add(12, 9), 21)

    def test_subtrtact(self):
        self.assertEquals(subtract(50, 25), 25)
        self.assertEquals(subtract(-40, 32), -72)

    def test_multiply(self):
        self.assertEquals(multiply(50, 2), 100)
        self.assertEquals(multiply(-4, -3), 12)

    def test_divide(self):
        self.assertEquals(divide(50, 2), 25)
        self.assertEquals(divide(40, 10), 4)
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()
