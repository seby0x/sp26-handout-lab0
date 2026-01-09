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