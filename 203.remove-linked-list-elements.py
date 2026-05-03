#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (54.35%)
# Likes:    9079
# Dislikes: 293
# Total Accepted:    1.6M
# Total Submissions: 2.9M
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Given the head of a linked list and an integer val, remove all the nodes of
# the linked list that has Node.val == val, and return the new head.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [], val = 1
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [7,7,7,7], val = 7
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 10^4].
# 1 <= Node.val <= 50
# 0 <= val <= 50
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建虚拟头节点，方便处理原 head 也需要被删除的情况
        dummy = ListNode(-1, head)

        # cur 始终指向“待检查节点”的前一个节点
        cur = dummy

        # 只要 cur 后面还有节点，就继续检查 cur.next
        while cur.next:
            # 如果下一个节点的值等于 val，就跳过这个节点
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                # 如果下一个节点不需要删除，cur 才向后移动
                cur = cur.next

        # 返回删除后的新头节点
        return dummy.next
    

# @lc code=end

