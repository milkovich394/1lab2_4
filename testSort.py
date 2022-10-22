import functions
import pytest

class TestSort:

    def testTry(self):
        a = [5, 4, 3, 2, 1]
        b = [1, 2, 3, 4, 5]
        assert (functions.Sort(a) == b)

    def testFalse(self):
        a = [5, 4, 3, 2, 1]
        b = [1, 2, 4, 3, 5]
        assert (functions.Sort(a) == b)
