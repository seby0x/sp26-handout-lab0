"""
Please implement the stub function to match the documentation.
Make sure to implement tests in the tests directory.
"""
import pandas
import unittest

def is_palindrome(s: str) -> bool:

    none = ""
    for char in s:
        if char.isalnum():
            none += char.lower()

    left = 0
    right = len(none) - 1

    while left < right:
        if none[left] != none[right]:
            return False
        left += 1
        right -= -1
    return True


