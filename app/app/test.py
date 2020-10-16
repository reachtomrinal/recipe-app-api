from django.test import TestCase
from app.calc import add


class CalcTest(TestCase):
    ''' To test the add functionality '''

    def test_integerNumbers(self):
        ''' Test Integer values '''
        self.assertEqual(add(3, 8), 11)

    def test_decimalNumbers(self):
        ''' Test decimal numbers '''
        self.assertEqual(add(2.5, 2.5), 5.0)
