"""Tests for Lab 0 Question 1"""
import pandas
import sys
sys.path.append(".")
import unittest
from src.q1 import is_palindrome

def add(num1: int, num2) -> int:
    return num1 + num2

result: str = add(3, 'hi')

def func() -> int:
    pass


#under here is my test for the function

class tester(unittest.TestCase):
    "tests the palindrome function"

    def test_is_palindrome(self) -> None:
        """tests for palindrome function"""
        self.assertTrue("racecar")
        self.assertFalse("spaghetti")