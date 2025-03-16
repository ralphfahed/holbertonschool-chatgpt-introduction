#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1: #this is the condition , so just we need n -= 1 to make n reach 1 and stop the loop.
        result *= n
        n -= 1  # Decrement n to avoid infinite loop
    return result

# sys.argv is a list that stores command-line arguments.
# sys.argv[0] is always the script name (factorial.py).
# sys.argv[1] is the first argument passed by the user when running the script

f = factorial(int(sys.argv[1]))
print(f)
