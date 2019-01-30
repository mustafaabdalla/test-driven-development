from calculator import Calculator
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()


    def test_add_method(self):

        """ this function checks if the values passed will returns the right answers"""

        result = self.calculator.add(1,2)
        
        self.assertEqual(3,result) 