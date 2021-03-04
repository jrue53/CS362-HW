import pytest


def fib(n):
    x = 0
    y = 1
    z = 0
    if n < 0:
        print("N is too small!")
        return None
    elif n == 0 or n == 1:
        return n
    else:
        for i in range(n - 1):
            z = x + y
            x = y
            y = z
        return z

def factorial(n):
    if n < 0:
        print ("N is too small!")
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
    return fact

def test_answer():
    assert fib(3) == 3

    assert fib(-1) == None

    assert fib(0) == 0

    assert fib(1) == 1 
