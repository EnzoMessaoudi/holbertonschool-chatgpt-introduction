#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Recursively calculates the factorial of a non-negative integer n.
        The factorial of n (n!) is the product of all positive integers up to n.
        By definition, 0! is 1.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the given integer n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(sys.argv[1])

f = factorial(n)
print(f)
