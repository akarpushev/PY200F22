import unittest


def add(x, y):
    return x + y


class TestSum(unittest.TestCase): # наследование от unittest.TestCase

    def test_add(self): # сохраняется имя функции add
        self.assertEqual(add(1, 2), 3) # проверяет равенство
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)


if __name__ == '__main__':
    unittest.main()
