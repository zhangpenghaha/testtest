import unittest

def add(a, b):
    return a + b

class TestAssert(unittest.TestCase):

    def test01(self):
        result = add(1, 1)
        print(result)
        self.assertEqual(3 , result)