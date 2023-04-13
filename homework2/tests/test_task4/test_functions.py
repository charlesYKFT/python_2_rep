"""A bunch of functions which were created to test task4"""

def sum_of_two(a, b):
    "Return the sum of two numbers"
    return a + b


def multiply(a, b):
    "Return the multiplication of two numbers"
    return a * b


def squaring(a):
    "Return the square of the number"
    return a**2


def gcd(a, b):
    "Returns gcd(НОД) of two numbers"
    a = 50
    b = 130

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a
