import unittest
from ProjMod import *



class CalcTest(unittest.TestCase):

    def test_one(self):
        self.assertEqual(one(1), 1)
        self.assertEqual(one(5), 15)

        with self.assertRaises(TypeError):
            one('7.5')

    def test_two(self):
        self.assertEqual(two(5, 0), 1)
        self.assertEqual(two(7, 2), 49)

        with self.assertRaises(TypeError):
            two('7.5', 0)
            two(1, '7.5')



    def test_three(self):
        self.assertEqual(three(2), None)

        with self.assertRaises(TypeError):
            three('1')
            three(1.5)
            three(0)


if __name__ == '__main__':
    unittest.main()
