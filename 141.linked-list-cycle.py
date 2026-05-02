#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (54.24%)
# Likes:    17580
# Dislikes: 1592
# Total Accepted:    4.9M
# Total Submissions: 9M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given head, the head of a linked list, determine if the linked list has a
# cycle in it.
# 
# There is a cycle in a linked list if there is some node in the list that can
# be reached again by continuously following the next pointer. Internally, pos
# is used to denote the index of the node that tail's next pointer is connected
# to. Note that pos is not passed as a parameter.
# 
# Return true if there is a cycle in the linked list. Otherwise, return
# false.
# 
# 
# Example 1:
# 
# 
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 1st node (0-indexed).
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 0th node.
# 
# 
# Example 3:
# 
# 
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
# 
# 
# 
# Constraints:
# 
# 
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.
# 
# 
# 
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 方法一：使用哈希表（set）记录访问过的节点
        # 时间复杂度 O(n)，空间复杂度 O(n)
        # curr 用来遍历链表
        curr = head

        # visited 用来记录已经访问过的节点对象
        visited = set()

        # 如果链表没有环，curr 最终会走到 None，循环结束
        # 如果链表有环，curr 会再次走到某个访问过的节点
        while curr:
            # 当前节点已经出现过，说明存在环
            if curr in visited:
                return True

            # 记录当前节点
            visited.add(curr)

            # 继续访问下一个节点
            curr = curr.next

        # 能走到 None，说明链表没有环
        return False
# @lc code=end

