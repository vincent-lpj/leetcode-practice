#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (80.49%)
# Likes:    24570
# Dislikes: 585
# Total Accepted:    6.3M
# Total Submissions: 7.8M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: [2,1]
# 
# 
# Example 3:
# 
# 
# Input: head = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
# 
# 
# 
# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 头插法
        # 我们创建一个虚拟头节点dummy，然后遍历链表，将每个节点依次插入dummy的下一个节点。
        # 遍历结束，返回dummy.next。时间复杂度O(n)，其中n为链表的长度。空间复杂度O(1)。

        # 创建一个虚拟头节点
        # dummy.next 始终指向“反转后链表”的头节点
        dummy = ListNode()

        # curr 用来遍历原链表
        curr = head

        while curr:
            # 先保存 curr 的下一个节点
            # 因为后面会修改 curr.next，如果不先保存，就会丢失后面的链表
            nxt = curr.next

            # 头插法第一步：
            # 让当前节点 curr 指向已经反转好的链表头
            curr.next = dummy.next

            # 头插法第二步：
            # 让 dummy.next 指向 curr
            # 这样 curr 就被插到了反转链表的最前面
            dummy.next = curr

            # 继续处理原链表中的下一个节点
            curr = nxt

        # dummy.next 就是反转后的新头节点
        return dummy.next
    
            
# @lc code=end

