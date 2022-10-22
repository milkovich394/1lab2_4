import functions
import pytest
import numpy as numpy

class TestFib:

    def testTry(self):
        arr = numpy.array([0, 1, 1, 2, 3, 5])
        assert (functions.Fib(5) == arr).all()

    def testFalse(self):
        arr = numpy.array([0, 1, 1, 2, 3, 4])
        assert  (functions.Fib(5) == arr).all()
