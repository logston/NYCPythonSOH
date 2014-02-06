"""
Python Exercise Set
===================

NYC Python Meetup - 2014/02/08
------------------------------

2013 Paul Logston
This module is provided is placed in the public domain as of the 
time of its publication in a publicly accessible location.

Brownie points for graphing the hash.
"""
import unittest


def generate_hash(hash, max):
    """
    Populate ``hash`` with key-value pairs where the keys are integers 
    between 1 and ``max`` and a key's value is the number of primes
    required to produce the key when the primes are
    multiplied together.

    For example:
    - A key of 1 would have a value of 1.
    - A key of 2 would have a value of 1.
    - A key of 4 would have a value of 2; 2 and 2.
    - A key of 8 would have a value of 3; 2 and 2 and 2.
    - A key of 95 would have a value of 2; 5 and 19.
    """

    # Build me!

class HashTestCase(unittest.TestCase):
    """
    These are some tests that you can run to check your work.
    """
    def setUp(self):
        self.hash = {}
        generate_hash(self.hash, 100)

    def test_1(self):
        self.assertIn(1, self.hash)
        self.assertEqual(self.hash[1], 1)

    def test_2(self):
        self.assertIn(2, self.hash)
        self.assertEqual(self.hash[2], 1)

    def test_4(self):
        self.assertIn(4, self.hash)
        self.assertEqual(self.hash[4], 2)

    def test_8(self):
        self.assertIn(8, self.hash)
        self.assertEqual(self.hash[8], 3)

    def test_27(self):
        self.assertIn(27, self.hash)
        self.assertEqual(self.hash[27], 3)

    def test_95(self):
        self.assertIn(95, self.hash)
        self.assertEqual(self.hash[95], 2)


if __name__ == '__main__':
    unittest.main()