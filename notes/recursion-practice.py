# Recursion Practice Problems
# Write your solution below each problem.

# --------------------------------------------------
# Problem 1: Factorial
# Given a non-negative integer n, return n! (n factorial).
# factorial(0) = 1
# factorial(5) = 120
#
# Hint:
#   Base case: factorial(0) = 1
#   Breakdown: factorial(n) = n * factorial(n - 1)
# --------------------------------------------------


# --------------------------------------------------
# Problem 2: Fibonacci
# Given n, return the nth Fibonacci number (0-indexed).
# fib(0) = 0, fib(1) = 1, fib(6) = 8
#
# Hint:
#   Base case: fib(0) = 0, fib(1) = 1
#   Breakdown: fib(n) = fib(n - 1) + fib(n - 2)
# --------------------------------------------------


# --------------------------------------------------
# Problem 3: Sum of List
# Given a list of integers, return the sum of all elements using recursion.
# sum_list([1, 2, 3, 4]) = 10
#
# Hint:
#   Base case: empty list returns 0
#   Breakdown: sum = first element + sum_list(rest of list)
# --------------------------------------------------


# --------------------------------------------------
# Problem 4: Reverse a String
# Given a string, return the reversed string using recursion.
# reverse("hello") = "olleh"
#
# Hint:
#   Base case: empty string or single character returns itself
#   Breakdown: reverse(s) = reverse(s[1:]) + s[0]
# --------------------------------------------------


# --------------------------------------------------
# Problem 5: Power
# Given base b and exponent e (non-negative integer), return b^e using recursion.
# power(2, 10) = 1024
#
# Hint:
#   Base case: any number to the power of 0 is 1
#   Breakdown: power(b, e) = b * power(b, e - 1)
# --------------------------------------------------


# --------------------------------------------------
# Problem 6: Count Occurrences
# Given a list and a target value, return how many times the target appears using recursion.
# count([1, 2, 3, 2, 2], 2) = 3
#
# Hint:
#   Base case: empty list returns 0
#   Breakdown: check if first element equals target (add 1 or 0), then count(rest, target)
# --------------------------------------------------


# --------------------------------------------------
# Problem 7: Flatten Nested List
# Given a nested list of integers (arbitrarily deep), return a flat list.
# flatten([1, [2, [3, 4], 5], 6]) = [1, 2, 3, 4, 5, 6]
#
# Hint:
#   Base case: empty list returns []
#   Breakdown: if first element is a list, flatten it recursively;
#              otherwise wrap it in [] and concatenate with flatten(rest)
# --------------------------------------------------


# ==================================================
# SOLUTIONS
# ==================================================

# Solution 1: Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Solution 2: Fibonacci
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# Solution 3: Sum of List
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])


# Solution 4: Reverse a String
def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]


# Solution 5: Power
def power(b, e):
    if e == 0:
        return 1
    return b * power(b, e - 1)


# Solution 6: Count Occurrences
def count(lst, target):
    if not lst:
        return 0
    return (1 if lst[0] == target else 0) + count(lst[1:], target)


# Solution 7: Flatten Nested List
def flatten(lst):
    if not lst:
        return []
    head = lst[0]
    if isinstance(head, list):
        return flatten(head) + flatten(lst[1:])
    return [head] + flatten(lst[1:])
