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


# ==================================================
# EXPLANATIONS
# ==================================================

# --- Problem 1: Factorial ---
#
# Approach:
#   Multiply n by the result of the smaller subproblem factorial(n-1).
#   The call stack unwinds from n=0 back up to n, multiplying at each level.
#   Call stack for factorial(3): 3 * (2 * (1 * (1))) = 6
#
# LeetCode application:
#   Factorial itself rarely appears directly, but the pattern — "solve for n
#   by assuming you already have the answer for n-1" — is the foundation of
#   almost every recursive problem (tree traversal, DFS, divide & conquer).
#
# Extensions & common patterns:
#   - Optimize with memoization to avoid redundant calls (top-down DP)
#   - Iterative version with a running product (bottom-up DP)
#   - Permutation count uses n! directly (#46 Permutations)


# --- Problem 2: Fibonacci ---
#
# Approach:
#   Each call branches into two smaller subproblems. The tree of calls has
#   height n, but without memoization many subproblems are recomputed,
#   giving O(2^n) time — exponential and slow for large n.
#
# LeetCode application:
#   The naive recursion is a classic example of why memoization matters.
#   The same "two branches" pattern appears in:
#     - #70 Climbing Stairs (reach step n from n-1 or n-2)
#     - #746 Min Cost Climbing Stairs
#
# Extensions & common patterns:
#   - Add a memo dict (top-down DP) to reduce to O(n) time
#   - Rewrite as a loop with two variables (bottom-up DP, O(1) space)
#   - Any problem where the answer depends on the previous two states
#     follows this exact structure


# --- Problem 3: Sum of List ---
#
# Approach:
#   Peel off the first element and add it to the sum of the remaining list.
#   This "head + recurse on tail" pattern works on any sequential structure.
#
# LeetCode application:
#   Directly mirrors linked list recursion:
#     - #206 Reverse Linked List (process head, recurse on head.next)
#     - #203 Remove Linked List Elements
#     - #234 Palindrome Linked List
#   In all these problems, lst[0] becomes node.val and lst[1:] becomes node.next.
#
# Extensions & common patterns:
#   - Replace "sum" with any accumulation: max, min, product, string join
#   - Works on trees too: sum of all node values = root.val + sum(left) + sum(right)
#   - Note: lst[1:] creates a new list each call (O(n) space per call).
#     For efficiency, pass an index instead: sum_list(lst, index)


# --- Problem 4: Reverse a String ---
#
# Approach:
#   Move the first character to the end, then reverse the rest.
#   reverse("hello") = reverse("ello") + "h" = "olle" + "h" = "olleh"
#
# LeetCode application:
#   - #344 Reverse String (in-place with two pointers, but recursive version
#     is a good warm-up)
#   - #206 Reverse Linked List uses the same idea: recurse to the end,
#     then re-link nodes on the way back up
#   - #234 Palindrome Linked List checks if a string/list reads the same
#     forwards and backwards
#
# Extensions & common patterns:
#   - Palindrome check: reverse(s) == s
#   - Two-pointer approach is more efficient (O(1) space) for in-place reversal
#   - The "do work on the way back up" pattern is key for many tree problems


# --- Problem 5: Power ---
#
# Approach:
#   Multiply b by itself e times by reducing e by 1 each call.
#   This naive version runs in O(e) time.
#
# LeetCode application:
#   - #50 Pow(x, n) — the direct LeetCode version of this problem.
#     The naive solution passes, but the optimal approach is fast exponentiation.
#
# Extensions & common patterns:
#   Fast exponentiation (O(log e)) — a crucial optimization:
#     if e is even:  power(b, e) = power(b * b, e // 2)
#     if e is odd:   power(b, e) = b * power(b, e - 1)
#   This halves the problem size each step instead of reducing by 1.
#   The same divide-and-conquer idea appears in merge sort and binary search.


# --- Problem 6: Count Occurrences ---
#
# Approach:
#   Check the first element, contribute 0 or 1, then recurse on the rest.
#   This is the general pattern for "scan every element and accumulate."
#
# LeetCode application:
#   - Any problem that traverses a tree/list and counts nodes matching a
#     condition uses this exact structure:
#     #700 Search in a BST, #112 Path Sum, #257 Binary Tree Paths
#   - In tree form: count(node) = match(node) + count(left) + count(right)
#
# Extensions & common patterns:
#   - Swap "count" for "filter" to collect matching elements instead
#   - Swap "==" for any predicate (e.g., count even numbers, count negatives)
#   - Works unchanged on trees by adding a second recursive call for the
#     right child


# --- Problem 7: Flatten Nested List ---
#
# Approach:
#   Inspect the first element. If it is itself a list, recursively flatten it
#   before concatenating. This handles arbitrary nesting depth because each
#   recursive call either reduces the list length or reduces the nesting depth.
#
# LeetCode application:
#   - #341 Flatten Nested List Iterator — the direct LeetCode version.
#     Uses the same isinstance check but returns an iterator instead of a list.
#   - #114 Flatten Binary Tree to Linked List — same concept on a tree:
#     recursively flatten left and right subtrees, then re-link.
#   - #430 Flatten a Multilevel Doubly Linked List
#
# Extensions & common patterns:
#   - isinstance() is the key tool whenever input can be heterogeneous
#     (mixed scalars and containers)
#   - The pattern generalizes to any recursive data structure (JSON, AST nodes)
#   - For very deep nesting, consider an iterative stack-based approach to
#     avoid Python's recursion depth limit
