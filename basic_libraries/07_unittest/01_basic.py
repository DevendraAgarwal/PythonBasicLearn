import unittest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Divide By Zero Not Valid")
    return round(a/b, 2)

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 1)

    def test_divide_function(self):
        self.assertEqual(divide(10, 3), 3.33)
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-10, 5), -2)
        self.assertEqual(divide(10, -5), -2)
        self.assertEqual(divide(-10, -5), 2)

    def test_divide_with_exception(self):
        
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()