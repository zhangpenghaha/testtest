import unittest
from parameterized import parameterized

def add(a, b):
    return a+b

def data():
    return [(1,2,3),(2,2,4),(4,4,8)]

class TestAdd(unittest.TestCase):

    @parameterized.expand(data)
    def test_add01(self,a,b,expect):
        result = add(a,b)
        self.assertEqual(result, expect)