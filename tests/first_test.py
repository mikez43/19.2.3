import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_mult(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_mult2(self):
        assert self.calc.multiply(self, 3, 4) == 12

    def test_sum(self):
        assert  self.calc.adding(self, 2, 3) == 5

    def test_sum2(self):
        assert self.calc.adding(self, 5, 2) == 7

    def test_div(self):
        assert  self.calc.division(self, 6, 3) == 2

    def test_div2(self):
        assert  self.calc.division(self, -3, 3) == -1

    def test_sub(self):
        assert  self.calc.subtraction(self, 7, 3) == 4

    def test_sub2(self):
        assert  self.calc.subtraction(self, 2, 3) == -1
