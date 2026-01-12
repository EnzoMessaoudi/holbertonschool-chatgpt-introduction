#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) != 2:
    print("Not enought arguments passed")
    sys.exit(1)

n = int(sys.argv[1])
if(n < 0):
        print("Passed a negative value")
        sys.exit(1)

f = factorial(n)
print(f)