"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert calculator.add(2, 2) == 4

    def test_subtraction(self):
        assert calculator.subtract(4, 2) == 2

    def test_multiplicatin(self):
        assert 100 = calculator.multiply(10, 10)
