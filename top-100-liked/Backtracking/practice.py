# Backtracking Practice Problems
# Three classic patterns from the 6 solved problems.
# Try to solve each one from scratch before reading the hints.

# ============================================================
# PATTERN 1: Subsets / Combinations (order doesn't matter)
# Use a `start` index so you only pick elements ahead of you.
# ============================================================

# Problem 1A: Subsets
# Given a list of unique integers, return all possible subsets (including []).
# Input:  nums = [1, 2, 3]
# Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]  (any order)
#
# Hint: at each index, make two choices — skip or pick — then move forward.

def subsets(nums):
    # Pattern: binary choice at each index (skip or pick)
    # Base case: index reaches end of nums
    # No pruning needed — every path is a valid subset
    pass


# Problem 1B: Combination Sum (Simple)
# Given a list of distinct positive integers and a target,
# return all unique combinations that sum to target.
# Each number can be used multiple times.
# Input:  candidates = [2, 3, 5], target = 6
# Output: [[2,2,2], [2,4]... wait, 4 not in list. Correct: [[2,2,2],[3,3]]
#
# Hint: pass `start` index and `remaining` sum; prune when remaining < 0.

def combination_sum(candidates, target):
    # Pattern: for-loop over candidates from `start`, track remaining sum
    # Base case: remaining == 0
    # Prune: remaining < 0
    # Note: pass i (not i+1) to allow reusing the same element
    pass


# ============================================================
# PATTERN 2: Permutations (order matters)
# Each element used exactly once; pick from whatever is still available.
# ============================================================

# Problem 2: Permutations
# Given a list of distinct integers, return all possible permutations.
# Input:  nums = [1, 2, 3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Hint: maintain a `remaining` list; when it's empty, record the path.

def permutations(nums):
    # Pattern: for-loop over all remaining elements (no start index)
    # Base case: remaining list is empty
    # No pruning needed — all orderings are valid
    pass


# ============================================================
# PATTERN 3: Constraint Pruning
# Build the answer character by character; prune invalid branches early.
# ============================================================

# Problem 3A: Generate Parentheses (Mini version, n=2)
# Given n, generate all valid combinations of n pairs of parentheses.
# Input:  n = 2
# Output: ["(())", "()()"]
#
# Hint: track open_count and close_count.
#       Prune if open_count > n, or close_count > open_count.

def generate_parentheses(n):
    # Pattern: track open_count and close_count, try adding "(" or ")"
    # Base case: path length == 2 * n
    # Prune: open_count > n  OR  close_count > open_count
    pass


# Problem 3B: Palindrome Partitioning (Short string)
# Partition string s so that every substring is a palindrome.
# Return all possible partitions.
# Input:  s = "aab"
# Output: [["a","a","b"], ["aa","b"]]
#
# Hint: try every end position from `index`; only recurse if s[index:end] is a palindrome.

def palindrome_partitioning(s):
    # Pattern: for-loop over all end positions from current index
    # Base case: index reaches end of s
    # Prune: skip if s[index:end] is not a palindrome
    pass


# ============================================================
# REFERENCE ANSWERS (try on your own first!)
# ============================================================

def _subsets(nums):
    result = []
    path = []

    def dfs(index):
        if index == len(nums):
            result.append(path[:])
            return
        # skip nums[index]
        dfs(index + 1)
        # pick nums[index]
        path.append(nums[index])
        dfs(index + 1)
        path.pop()

    dfs(0)
    return result


def _combination_sum(candidates, target):
    result = []
    path = []

    def dfs(start, remaining):
        if remaining < 0:
            return
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            dfs(i, remaining - candidates[i])
            path.pop()

    dfs(0, target)
    return result


def _permutations(nums):
    result = []
    path = []

    def dfs(remaining):
        if not remaining:
            result.append(path[:])
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            dfs(remaining[:i] + remaining[i+1:])
            path.pop()

    dfs(nums)
    return result


def _generate_parentheses(n):
    result = []

    def dfs(open_count, close_count, path):
        if open_count > n or close_count > open_count:
            return
        if len(path) == 2 * n:
            result.append(path)
            return
        dfs(open_count + 1, close_count, path + "(")
        dfs(open_count, close_count + 1, path + ")")

    dfs(0, 0, "")
    return result


def _palindrome_partitioning(s):
    result = []
    path = []

    def dfs(index):
        if index == len(s):
            result.append(path[:])
            return
        for end in range(index + 1, len(s) + 1):
            substring = s[index:end]
            if substring != substring[::-1]:
                continue
            path.append(substring)
            dfs(end)
            path.pop()

    dfs(0)
    return result


# ============================================================
# Test cases — uncomment to check your solutions
# ============================================================

print(subsets([1, 2, 3]))
# Expected (any order): [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

print(combination_sum([2, 3, 5], 6))
# Expected (any order): [[2,2,2], [3,3]]

print(permutations([1, 2, 3]))
# Expected (any order): [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

print(generate_parentheses(2))
# Expected (any order): ["(())", "()()"]

print(palindrome_partitioning("aab"))
# Expected (any order): [["a","a","b"], ["aa","b"]]