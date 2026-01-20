# calculator.py

import math 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("You cannot divide by 0")
    return a / b   

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        print("Your square root cannot be negative")
    return math.sqrt(a)

