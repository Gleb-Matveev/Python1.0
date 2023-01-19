from unittest import TestCase, main
from main import calc


class CalcTest(TestCase):
    def test_add(self):
        self.assertEqual(3, calc(1, 2, "+"))
        self.assertEqual(15, calc(7, 8, "+"))
        self.assertEqual(20, calc(-1, 21, "+"))

    def test_sub(self):
        self.assertEqual(-1, calc(1, 2, "-"))
        self.assertEqual(-1, calc(7, 8, "-"))
        self.assertEqual(-22, calc(-1, 21, "-"))

    def test_div(self):
        self.assertEqual(1, calc(2, 2, "/"))
        self.assertEqual(4, calc(32, 8, "/"))
        self.assertEqual("undefined", calc(21, 0, "/"))

    def test_mul(self):
        self.assertEqual(2, calc(1, 2, "*"))
        self.assertEqual(56, calc(7, 8, "*"))
        self.assertEqual(-21, calc(-1, 21, "*"))

if __name__ == '__main__':
    main()
