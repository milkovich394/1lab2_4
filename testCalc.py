import functions
import pytest

class TestCalc:

    def testTry(self):
        assert functions.Calc(3, 2, '+') == 5

    def testFalse(self):
        assert functions.Calc(3, 2, '+') == 2
