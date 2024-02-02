import unittest
from add import Calculator


class TestStringMethods(unittest.TestCase):
    print("TestString")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO') # сравнение

    def test_isupper(self):
        self.assertTrue('FOO'.isupper()) # True или не True
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)



calc = Calculator(5)
calc.set_color('red')
class TestCalculator(unittest.TestCase):
    print("TestCalculator")

    def test_add(self):
        print("test_add")
        self.assertEqual(Calculator.add(5, 3), 8)

    def test_color(self):
        # print("test_add")
        # self.assertTrue('FOO'.isupper())
        # self.assertFalse('Foo'.isupper())
        self.assertEqual(calc.set_color('red'), calc.color) # ??????


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
