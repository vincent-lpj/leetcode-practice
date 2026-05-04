# Python Data Structures — LeetCode Practice
# Each section covers one data type with exercises commonly seen in LeetCode.
# Write your answer below each problem, then run the file to check.

from collections import defaultdict, Counter, deque
import heapq


# ==================================================
# SECTION 1: Dictionary (dict)
# ==================================================

d = {"a": 1, "b": 2, "c": 3}
nums = [1, 2, 2, 3, 3, 3]
words = ["cat", "dog", "hi", "go", "elephant"]

# --------------------------------------------------
# 1-0: Basic Operations
# Using d = {"a": 1, "b": 2, "c": 3}:
#   a) Access the value for key "b"               -> 2
#   b) Add a new key "d" with value 4
#   c) Delete the key "a"
#   d) Get value for key "z" with default 0       -> 0
#   e) Print all keys                             -> dict_keys(["b", "c", "d"])
#   f) Print all values
#   g) Print all key-value pairs as tuples
# --------------------------------------------------
# a)

# b)

# c)

# d)

# e)

# f)

# g)


# --------------------------------------------------
# 1-1: Frequency Count
# Given nums = [1, 2, 2, 3, 3, 3], return a dict mapping each number to its frequency.
# Output: {1: 1, 2: 2, 3: 3}
# Hint:   freq.get(n, 0) + 1
# --------------------------------------------------


# --------------------------------------------------
# 1-2: Iterate Over a Dict
# Given d = {"a": 1, "b": 2, "c": 3}, print each pair as "key -> value".
# Output: a -> 1 \n b -> 2 \n c -> 3
# --------------------------------------------------


# --------------------------------------------------
# 1-3: Invert a Dict
# Given d = {"a": 1, "b": 2, "c": 3}, return a new dict with keys and values swapped.
# Output: {1: "a", 2: "b", 3: "c"}
# Hint:   dict comprehension  {v: k for k, v in ...}
# --------------------------------------------------


# --------------------------------------------------
# 1-4: Group by Property (defaultdict)
# Given words = ["cat", "dog", "hi", "go", "elephant"], group them by length.
# Output: {3: ["cat", "dog"], 2: ["hi", "go"], 8: ["elephant"]}
# Hint:   defaultdict(list)
# --------------------------------------------------


# --------------------------------------------------
# 1-5: Two Sum with Dict  (LeetCode #1)
# nums = [2, 7, 11, 15], target = 9 -> [0, 1]
# Hint:   For each number, check if (target - number) is already in a seen dict
# --------------------------------------------------
two_sum_nums, two_sum_target = [2, 7, 11, 15], 9


# ==================================================
# SECTION 2: Counter
# ==================================================

lst = [1, 1, 2, 2, 2, 3]
s1, s2 = "anagram", "nagaram"

# --------------------------------------------------
# 2-0: Basic Operations
# Using lst = [1, 1, 2, 2, 2, 3]:
#   a) Create a Counter from lst
#   b) Access the count of element 2              -> 3
#   c) Get the 2 most common elements             -> [(2, 3), (1, 2)]
#   d) Convert Counter back to a regular dict
# --------------------------------------------------
# a)

# b)

# c)

# d)


# --------------------------------------------------
# 2-1: Most Common Elements
# Given lst = [1, 1, 2, 2, 2, 3], return the 2 most common as [[val, count], ...].
# Output: [[2, 3], [1, 2]]
# --------------------------------------------------


# --------------------------------------------------
# 2-2: Anagram Check  (LeetCode #242)
# s1 = "anagram", s2 = "nagaram" -> True
# --------------------------------------------------


# ==================================================
# SECTION 3: Set
# ==================================================

a = [3, 1, 2, 1, 3]
b, c = [1, 2, 3, 4], [3, 4, 5, 6]

# --------------------------------------------------
# 3-0: Basic Operations
# Using a = [3, 1, 2, 1, 3]:
#   a) Create a set from a
#   b) Add element 9 to the set
#   c) Remove element 1 (raises error if missing — use discard to be safe)
#   d) Check if 2 is in the set                   -> True
#   e) Union of {1, 2, 3} and {3, 4, 5}           -> {1, 2, 3, 4, 5}
#   f) Difference of {1, 2, 3} and {3, 4, 5}      -> {1, 2}
# --------------------------------------------------
# a)

# b)

# c)

# d)

# e)

# f)


# --------------------------------------------------
# 3-1: Remove Duplicates
# Given a = [3, 1, 2, 1, 3], return a sorted list with duplicates removed.
# Output: [1, 2, 3]
# --------------------------------------------------


# --------------------------------------------------
# 3-2: Intersection
# Given b = [1,2,3,4] and c = [3,4,5,6], return a sorted list of common elements.
# Output: [3, 4]
# --------------------------------------------------


# --------------------------------------------------
# 3-3: Contains Duplicate  (LeetCode #217)
# [1, 2, 3, 1] -> True  |  [1, 2, 3, 4] -> False
# --------------------------------------------------


# ==================================================
# SECTION 4: List & Slice
# ==================================================

lst4 = [10, 20, 30, 40, 50, 60, 70]

# --------------------------------------------------
# 4-0: Slicing & Indexing
# Using lst4 = [10, 20, 30, 40, 50, 60, 70]:
#   a) First element                              -> 10
#   b) Last element (negative index)              -> 70
#   c) First 3 elements                           -> [10, 20, 30]
#   d) Last 3 elements                            -> [50, 60, 70]
#   e) Every other element                        -> [10, 30, 50, 70]
#   f) Reversed list using slice                  -> [70, 60, 50, 40, 30, 20, 10]
#   g) Elements from index 2 to 5 (exclusive)     -> [30, 40, 50]
# --------------------------------------------------
# a)

# b)

# c)

# d)

# e)

# f)

# g)


# --------------------------------------------------
# 4-1: Basic List Methods
# Using lst4 = [10, 20, 30, 40, 50, 60, 70]:
#   a) Append 80 to the end
#   b) Insert 15 at index 1
#   c) Remove the element 30 by value
#   d) Pop the last element and print it
#   e) Find the index of element 40               -> 3 (after above mutations)
#   f) Sort a new list [3,1,4,1,5] in place
#   g) Return a sorted copy of [3,1,4,1,5] without mutating it
# --------------------------------------------------
# a)

# b)

# c)

# d)

# e)

# f)

# g)


# --------------------------------------------------
# 4-2: List Comprehension — Squares
# Input:  [1, 2, 3, 4, 5, 6]   Output: [4, 16, 36]  (squares of even numbers)
# --------------------------------------------------
comp_lst = [1, 2, 3, 4, 5, 6]


# --------------------------------------------------
# 4-3: Sort by Custom Key
# Sort ["banana", "apple", "fig", "kiwi", "pear"] by length then alphabetically.
# Output: ["fig", "kiwi", "pear", "apple", "banana"]
# Hint:   key=lambda x: (len(x), x)
# --------------------------------------------------
sort_lst = ["banana", "apple", "fig", "kiwi", "pear"]


# --------------------------------------------------
# 4-4: Flatten One Level
# Input:  [[1, 2], [3, 4], [5]]   Output: [1, 2, 3, 4, 5]
# Hint:   [x for sub in lst for x in sub]
# --------------------------------------------------
nested = [[1, 2], [3, 4], [5]]


# ==================================================
# SECTION 5: Deque
# ==================================================

# --------------------------------------------------
# 5-0: Basic Operations
#   a) Create a deque from [1, 2, 3]
#   b) appendleft(0)                              -> deque([0, 1, 2, 3])
#   c) append(4)                                  -> deque([0, 1, 2, 3, 4])
#   d) popleft()                                  -> returns 0
#   e) pop()                                      -> returns 4
#   f) Create a deque with maxlen=3, append 1,2,3,4 and print  -> deque([2, 3, 4])
# --------------------------------------------------
# a)

# b)

# c)

# d)

# e)

# f)


# --------------------------------------------------
# 5-1: Sliding Window Maximum  (LeetCode #239)
# nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3 -> [3, 3, 5, 5, 6, 7]
# Hint:   Monotone deque — store indices, keep decreasing order of values.
#         Pop right if new element >= nums[dq[-1]].
#         Pop left if dq[0] is outside the window (index < i - k + 1).
# --------------------------------------------------
win_nums, win_k = [1, 3, -1, -3, 5, 3, 6, 7], 3


# ==================================================
# SECTION 6: Heap (heapq)
# ==================================================

# --------------------------------------------------
# 6-0: Basic Operations
#   a) heapify a list [3, 1, 4, 1, 5] in place (min-heap)
#   b) heappush a new element 0
#   c) heappop — removes and returns the smallest element
#   d) Peek at the smallest without removing       -> heap[0]
#   e) Simulate a max-heap: push -3, -1, -4; pop and negate to get max
# --------------------------------------------------
# a)

# b)

# c)

# d)

# e)


# --------------------------------------------------
# 6-1: K Smallest Elements
# nums = [3, 1, 4, 1, 5, 9, 2, 6], k = 3 -> [1, 1, 2]
# Hint:   heapq.nsmallest(k, nums)
# --------------------------------------------------
heap_nums, heap_k = [3, 1, 4, 1, 5, 9, 2, 6], 3


# --------------------------------------------------
# 6-2: Kth Largest Element  (LeetCode #215)
# nums = [3, 2, 1, 5, 6, 4], k = 2 -> 5
# Hint:   Min-heap of size k; root is always the kth largest.
# --------------------------------------------------
kth_nums, kth_k = [3, 2, 1, 5, 6, 4], 2


# ==================================================
# SECTION 7: String Operations
# ==================================================

sentence = "  the sky is blue  "
word = "Hello, World!"
code = "abc"

# --------------------------------------------------
# 7-0: Basic String Methods
# Using sentence = "  the sky is blue  " and word = "Hello, World!":
#   a) strip whitespace from sentence             -> "the sky is blue"
#   b) upper() on word                            -> "HELLO, WORLD!"
#   c) lower() on word                            -> "hello, world!"
#   d) replace "sky" with "ocean" in sentence     -> "  the ocean is blue  "
#   e) split sentence into words (strip first)    -> ["the", "sky", "is", "blue"]
#   f) join ["blue", "is", "sky", "the"] with " " -> "blue is sky the"
#   g) check if word startswith "Hello"           -> True
#   h) check if word endswith "???"               -> False
#   i) find index of "World" in word              -> 7
# --------------------------------------------------
# a)

# b)

# c)

# d)

# e)

# f)

# g)

# h)

# i)


# --------------------------------------------------
# 7-1: Reverse Words
# Input:  "the sky is blue"   Output: "blue is sky the"
# Hint:   split() -> slice [::-1] -> join()
# --------------------------------------------------
rev_sentence = "the sky is blue"


# --------------------------------------------------
# 7-2: Character Frequency with ord()
# Given code = "abc", return a list of 26 ints for frequency of each letter a-z.
# Output first 4 elements: [1, 1, 1, 0]
# Hint:   freq[ord(c) - ord('a')] += 1
# --------------------------------------------------


# ==================================================
# SECTION 8: int & Bit Operations
# ==================================================

n = 18   # binary: 10010
m = 6    # binary: 00110

# --------------------------------------------------
# 8-0: Arithmetic Basics
# Using n = 18, m = 6:
#   a) Integer division n // m                    -> 3
#   b) Remainder n % m                            -> 0
#   c) n to the power of 3                        -> 5832
#   d) Absolute value of -42                      -> 42
#   e) Convert n to binary string                 -> '0b10010'
#   f) Convert n to hex string                    -> '0x12'
#   g) float('inf') and float('-inf') — just print them
# --------------------------------------------------
# a)

# b)

# c)

# d)

# e)

# f)

# g)


# --------------------------------------------------
# 8-1: Bit Operations
# Using n = 18 (10010), m = 6 (00110):
#   a) AND  n & m                                 -> 2   (00010)
#   b) OR   n | m                                 -> 22  (10110)
#   c) XOR  n ^ m                                 -> 20  (10100)
#   d) Left shift  n << 1                         -> 36  (100100)
#   e) Right shift n >> 1                         -> 9   (01001)
#   f) Check if n is even using bitwise AND       -> True if (n & 1) == 0
# --------------------------------------------------
# a)

# b)

# c)

# d)

# e)

# f)


# --------------------------------------------------
# 8-2: Count Set Bits  (LeetCode #191)
# Given n = 18, count how many 1-bits are in its binary representation.
# 18 = 10010 -> 2
# Hint:   Use a loop: while n, add n & 1, then n >>= 1
#         OR: bin(n).count('1')
# --------------------------------------------------


# --------------------------------------------------
# 8-3: Power of Two  (LeetCode #231)
# Given n, return True if n is a power of 2.
# n = 16 -> True  |  n = 18 -> False
# Hint:   A power of 2 has exactly one set bit: n & (n - 1) == 0
# --------------------------------------------------
pow2_n = 16


# ==================================================
# SECTION 9: Tuple
# ==================================================

t = (3, 1, 4, 1, 5)
pairs = [(2, "b"), (1, "a"), (3, "c")]

# --------------------------------------------------
# 9-0: Basic Operations
# Using t = (3, 1, 4, 1, 5):
#   a) Access the first element                   -> 3
#   b) Slice the first 3 elements                 -> (3, 1, 4)
#   c) Count how many times 1 appears             -> 2
#   d) Find the index of value 5                  -> 4
#   e) Unpack t into five variables and print them
#   f) Unpack first element and the rest: first, *rest = t
#   g) Use a tuple as a dict key: {(0, 0): "origin"}
# --------------------------------------------------
# a)

# b)

# c)

# d)

# e)

# f)

# g)


# --------------------------------------------------
# 9-1: Sort by Second Element
# Given pairs = [(2, "b"), (1, "a"), (3, "c")], sort by the second element.
# Output: [(1, "a"), (2, "b"), (3, "c")]
# Hint:   key=lambda x: x[1]
# --------------------------------------------------


# --------------------------------------------------
# 9-2: Zip Two Lists into Tuples
# Given [1, 2, 3] and ["a", "b", "c"], produce [(1,"a"), (2,"b"), (3,"c")].
# Hint:   list(zip(a, b))
# --------------------------------------------------
zip_a = [1, 2, 3]
zip_b = ["a", "b", "c"]


# --------------------------------------------------
# 9-3: Coordinate Key in a Visited Set  (common in BFS/DFS grid problems)
# Given a grid path [(0,0), (0,1), (1,1)], use a set of tuples to track visited.
# Check if (0, 1) is already visited -> True
# Check if (2, 2) is already visited -> False
# --------------------------------------------------
path = [(0, 0), (0, 1), (1, 1)]


# ==================================================
# SECTION 10: Stack (list)
# ==================================================

# --------------------------------------------------
# 10-0: Basic Stack Operations
# A stack in Python is a list using append() and pop().
#   a) Create an empty stack
#   b) Push 1, 2, 3 onto the stack
#   c) Peek at the top without removing           -> stack[-1]
#   d) Pop the top element                        -> 3
#   e) Check if the stack is empty                -> False
#   f) Pop everything and print in order (LIFO)
# --------------------------------------------------
# a)

# b)

# c)

# d)

# e)

# f)


# --------------------------------------------------
# 10-1: Valid Parentheses  (LeetCode #20)
# Given a string of brackets, return True if every open bracket is closed
# in the correct order.
# "()"     -> True
# "()[]{}" -> True
# "(]"     -> False
# "([)]"   -> False
# Hint:   Push open brackets; on close bracket, check top of stack matches.
# --------------------------------------------------
parens_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]


# --------------------------------------------------
# 10-2: Evaluate Reverse Polish Notation  (LeetCode #150)
# Tokens are integers or operators "+", "-", "*", "/".
# Evaluate left to right; each operator applies to the top two stack values.
# ["2","1","+","3","*"] -> 9    ((2+1)*3)
# ["4","13","5","/","+"] -> 6  (4 + (13/5))
# Hint:   Push numbers; on operator, pop two, compute, push result.
#         Use int() for truncation toward zero: int(a / b)
# --------------------------------------------------
rpn = ["2", "1", "+", "3", "*"]


# --------------------------------------------------
# 10-3: Daily Temperatures  (LeetCode #739)
# Given a list of daily temperatures, return a list where each element is
# the number of days until a warmer temperature (0 if none).
# Input:  [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1,  1,  4,  2,  1,  1,  0,  0]
# Hint:   Monotone decreasing stack — store indices.
#         When a warmer day is found, pop and compute the gap.
# --------------------------------------------------
temps = [73, 74, 75, 71, 69, 72, 76, 73]


# ==================================================
# SOLUTIONS
# ==================================================

# --- 1-1 ---
def freq_count(lst):
    freq = {}
    for n in lst:
        freq[n] = freq.get(n, 0) + 1
    return freq

# --- 1-2 ---
def print_dict(d):
    for k, v in d.items():
        print(f"{k} -> {v}")

# --- 1-3 ---
def invert_dict(d):
    return {v: k for k, v in d.items()}

# --- 1-4 ---
def group_by_length(words):
    groups = defaultdict(list)
    for w in words:
        groups[len(w)].append(w)
    return dict(groups)

# --- 1-5 ---
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i

# --- 2-1 ---
def most_common(lst, k):
    return [[val, cnt] for val, cnt in Counter(lst).most_common(k)]

# --- 2-2 ---
def is_anagram(s, t):
    return Counter(s) == Counter(t)

# --- 3-1 ---
def remove_duplicates(lst):
    return sorted(set(lst))

# --- 3-2 ---
def intersection(a, b):
    return sorted(set(a) & set(b))

# --- 3-3 ---
def contains_duplicate(nums):
    return len(nums) != len(set(nums))

# --- 4-1 ---
def even_squares(lst):
    return [x ** 2 for x in lst if x % 2 == 0]

# --- 4-2 ---
def sort_by_length(words):
    return sorted(words, key=lambda x: (len(x), x))

# --- 4-3 ---
def flatten_one(lst):
    return [x for sub in lst for x in sub]

# --- 5-1 ---
def sliding_window_max(nums, k):
    dq = deque()
    result = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] <= n:
            dq.pop()
        dq.append(i)
        if dq[0] < i - k + 1:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

# --- 5-2 ---
def bfs_levels(start, levels):
    result = [start[:]]
    for level in levels:
        result.append(level[:])
    return result

# --- 6-1 ---
def k_smallest(nums, k):
    return sorted(heapq.nsmallest(k, nums))

# --- 6-2 ---
def kth_largest(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

# --- 7-1 ---
def reverse_words(s):
    return " ".join(s.split()[::-1])

# --- 7-2 ---
def char_freq(s):
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1
    return freq


# --- 8-2 ---
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# --- 8-3 ---
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# --- 9-1 ---
def sort_by_second(pairs):
    return sorted(pairs, key=lambda x: x[1])

# --- 9-2 ---
def zip_lists(a, b):
    return list(zip(a, b))

# --- 9-3 ---
def check_visited(path, query):
    visited = set(path)
    return query in visited

# --- 10-1 ---
def is_valid_parens(s):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack

# --- 10-2 ---
def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            b, a = stack.pop(), stack.pop()
            if token == "+": stack.append(a + b)
            elif token == "-": stack.append(a - b)
            elif token == "*": stack.append(a * b)
            else: stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]

# --- 10-3 ---
def daily_temperatures(temps):
    stack = []
    result = [0] * len(temps)
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result
