#!/usr/bin/python3
import sys

# Function description:
# This function calculates the factorial of a given number using recursion.
# The factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n.
# It is defined as:
#   factorial(n) = n * factorial(n-1), with the base case of factorial(0) = 1.

# Parameters:
#   n (int): The number for which the factorial is to be calculated. It must be a non-negative integer.

# Returns:
#   int: The factorial of the given number n.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Check if a command-line argument is provided
if len(sys.argv) < 2:
    print("Usage: ./factorial_recursive.py <number>")
    sys.exit(1)

# Convert the command line argument to an integer and calculate the factorial
try:
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)

