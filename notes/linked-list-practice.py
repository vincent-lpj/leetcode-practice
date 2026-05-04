# Linked List Practice Problems
# Write your solution below each problem.

# Standard node definition (same as LeetCode)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper: build a linked list from a Python list
def build(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper: convert a linked list back to a Python list (for printing)
def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# --------------------------------------------------
# Problem 1: Traverse a Linked List
# Print every value in the linked list.
# Input:  1 -> 2 -> 3 -> 4 -> 5
# Output: 1 2 3 4 5
#
# Hint:
#   Use a pointer starting at head, advance with curr = curr.next
#   Stop when curr is None
# --------------------------------------------------


# --------------------------------------------------
# Problem 2: Reverse a Linked List  (LeetCode #206)
# Given the head of a singly linked list, reverse it and return the new head.
# Input:  1 -> 2 -> 3 -> 4 -> 5
# Output: 5 -> 4 -> 3 -> 2 -> 1
#
# Hint:
#   Head-insertion pattern: keep a dummy new head, repeatedly take the
#   current node and insert it at the front
#   prev = None; while curr: save next, point curr.next to prev, advance
# --------------------------------------------------


# --------------------------------------------------
# Problem 3: Remove Linked List Elements  (LeetCode #203)
# Remove all nodes with val == target, return the new head.
# Input:  1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6,  target = 6
# Output: 1 -> 2 -> 3 -> 4 -> 5
#
# Hint:
#   Use a dummy head so you never need to special-case removing the real head
#   While traversing, if curr.next.val == target, skip it: curr.next = curr.next.next
# --------------------------------------------------


# --------------------------------------------------
# Problem 4: Detect a Cycle  (LeetCode #141)
# Return True if the linked list has a cycle, False otherwise.
#
# Hint:
#   Fast-slow pointer: slow moves 1 step, fast moves 2 steps
#   If they ever meet, there is a cycle
#   If fast reaches None, there is no cycle
# --------------------------------------------------


# --------------------------------------------------
# Problem 5: Find the Middle Node  (LeetCode #876)
# Return the middle node of the linked list.
# If there are two middles, return the second one.
# Input:  1 -> 2 -> 3 -> 4 -> 5   Output: node(3)
# Input:  1 -> 2 -> 3 -> 4        Output: node(3)
#
# Hint:
#   Fast-slow pointer: while fast and fast.next, advance both
#   When fast reaches None, slow is at the middle
# --------------------------------------------------


# --------------------------------------------------
# Problem 6: Remove Duplicates from Sorted List  (LeetCode #83)
# Given a sorted linked list, delete all duplicates so each value appears once.
# Input:  1 -> 1 -> 2 -> 3 -> 3
# Output: 1 -> 2 -> 3
#
# Hint:
#   While traversing, if curr.val == curr.next.val, skip next: curr.next = curr.next.next
#   Otherwise advance curr normally
# --------------------------------------------------


# --------------------------------------------------
# Problem 7: Merge Two Sorted Lists  (LeetCode #21)
# Merge two sorted linked lists and return the head of the merged list.
# Input:  1 -> 2 -> 4   and   1 -> 3 -> 4
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
#
# Hint:
#   Use a dummy head; compare the front nodes of both lists each step,
#   attach the smaller one, advance that pointer
#   After the loop, attach the remaining non-empty list
# --------------------------------------------------


# --------------------------------------------------
# Problem 8: Palindrome Linked List  (LeetCode #234)
# Return True if the linked list is a palindrome.
# Input:  1 -> 2 -> 2 -> 1   Output: True
# Input:  1 -> 2             Output: False
#
# Hint:
#   Step 1 — find the middle with fast-slow pointer
#             (use while fast.next and fast.next.next so slow stops at end of first half)
#   Step 2 — reverse the second half starting from slow.next
#   Step 3 — compare first half and reversed second half node by node
# --------------------------------------------------


# ==================================================
# SOLUTIONS
# ==================================================

# Solution 1: Traverse
def traverse(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()


# Solution 2: Reverse a Linked List
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


# Solution 3: Remove Linked List Elements
def remove_elements(head, target):
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.val == target:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next


# Solution 4: Detect a Cycle
def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


# Solution 5: Find the Middle Node
def middle_node(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# Solution 6: Remove Duplicates from Sorted List
def delete_duplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


# Solution 7: Merge Two Sorted Lists
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next


# Solution 8: Palindrome Linked List
def is_palindrome(head):
    # Step 1: find end of first half
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: reverse second half
    prev = None
    curr = slow.next
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second_half = prev

    # Step 3: compare
    p1, p2 = head, second_half
    while p2:
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next
    return True


# ==================================================
# EXPLANATIONS
# ==================================================

# --- Problem 1: Traverse ---
#
# Approach:
#   The most fundamental linked list operation. A pointer walks the chain
#   one node at a time via curr = curr.next until it hits None.
#   All other techniques below build on this basic traversal loop.
#
# LeetCode application:
#   Every linked list problem uses traversal internally.
#   Getting comfortable with the while curr / curr = curr.next pattern is
#   the prerequisite for everything else.


# --- Problem 2: Reverse a Linked List ---
#
# Approach:
#   Head-insertion (iterative): maintain a prev pointer initialized to None.
#   For each node, save its next, point it back to prev, then advance.
#   After the loop, prev is the new head.
#   Visualization: None <- 1  2 -> 3 -> ...
#                  None <- 1 <- 2  3 -> ...
#
# LeetCode application:
#   - #206 Reverse Linked List (this exact problem)
#   - #234 Palindrome Linked List (reverse second half)
#   - #25 Reverse Nodes in k-Group (reverse chunks)
#
# Extensions & common patterns:
#   - Recursive version: reverse(head.next), then head.next.next = head, head.next = None
#   - Reversing a sublist (between positions left and right) uses the same
#     three-pointer technique with extra bookkeeping for re-attachment


# --- Problem 3: Remove Linked List Elements ---
#
# Approach:
#   Dummy head eliminates the special case of removing the real head node.
#   Traverse with curr; whenever curr.next is a match, bypass it by setting
#   curr.next = curr.next.next. Only advance curr when no deletion occurs.
#
# LeetCode application:
#   - #203 Remove Linked List Elements
#   - #82 Remove Duplicates from Sorted List II (remove ALL duplicates)
#   - #19 Remove Nth Node From End of List (combines with two-pointer)
#
# Extensions & common patterns:
#   Dummy head is the standard setup for any problem that may delete the
#   head node. Always return dummy.next instead of head.


# --- Problem 4: Detect a Cycle ---
#
# Approach:
#   Floyd's cycle detection: slow moves 1 step, fast moves 2 steps.
#   If a cycle exists, fast "laps" slow and they meet inside the cycle.
#   If no cycle, fast reaches None first.
#   Time O(n), Space O(1) — much better than storing visited nodes in a set.
#
# LeetCode application:
#   - #141 Linked List Cycle
#   - #142 Linked List Cycle II (find the entry point of the cycle)
#   - #876 Middle of the Linked List (same two-pointer, no cycle)
#
# Extensions & common patterns:
#   To find the cycle entry (#142): after slow and fast meet, reset one
#   pointer to head and advance both one step at a time — they meet at the entry.


# --- Problem 5: Find the Middle Node ---
#
# Approach:
#   Same fast-slow setup as cycle detection, but the loop condition
#   while fast and fast.next ensures fast stops at the last node (odd length)
#   or goes past the end (even length), leaving slow at the middle.
#   Note: "while fast.next and fast.next.next" gives the first middle for
#   even-length lists — useful for palindrome problems.
#
# LeetCode application:
#   - #876 Middle of the Linked List
#   - #234 Palindrome Linked List (find first-half boundary)
#   - #148 Sort List (find midpoint to split for merge sort)
#
# Extensions & common patterns:
#   The two loop conditions give different midpoints for even-length lists.
#   Choose based on whether you need the first or second middle.


# --- Problem 6: Remove Duplicates from Sorted List ---
#
# Approach:
#   Because the list is sorted, duplicates are always adjacent.
#   Compare curr and curr.next: if equal, skip curr.next; otherwise advance.
#   No dummy head needed here since the real head is never removed.
#
# LeetCode application:
#   - #83 Remove Duplicates from Sorted List
#   - #82 Remove Duplicates from Sorted List II (harder: remove ALL nodes
#     with duplicate values, requires dummy head and extra bookkeeping)
#
# Extensions & common patterns:
#   The "skip while equal" pattern also appears in two-pointer problems on
#   sorted arrays (e.g., #26 Remove Duplicates from Sorted Array).


# --- Problem 7: Merge Two Sorted Lists ---
#
# Approach:
#   Dummy head gives a stable starting point. Compare the front nodes of
#   both lists, attach the smaller, advance that list's pointer, advance curr.
#   After one list is exhausted, attach the remainder of the other list directly
#   (no need to loop — it is already linked).
#
# LeetCode application:
#   - #21 Merge Two Sorted Lists
#   - #23 Merge k Sorted Lists (extend with a min-heap or divide-and-conquer)
#   - #148 Sort List (merge step of merge sort on a linked list)
#
# Extensions & common patterns:
#   This merge routine is the core of merge sort. Understanding it well is
#   the prerequisite for #148 (Sort List) and #23 (Merge k Sorted Lists).


# --- Problem 8: Palindrome Linked List ---
#
# Approach:
#   Combines two techniques from the notes:
#     1. Fast-slow pointer (find end of first half)
#     2. Head-insertion reversal (reverse second half in-place)
#   Then a simple two-pointer comparison walks both halves simultaneously.
#   The second half pointer p2 runs out first (or at the same time), which
#   handles both odd and even lengths correctly.
#
# LeetCode application:
#   - #234 Palindrome Linked List (this exact problem)
#
# Extensions & common patterns:
#   - In interviews, mention that you can restore the list by reversing the
#     second half again after comparison.
#   - The three-step pattern (find middle → reverse → compare) is a classic
#     linked list interview template worth memorising.


