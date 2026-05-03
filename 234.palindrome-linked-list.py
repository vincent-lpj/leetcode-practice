#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (57.86%)
# Likes:    18373
# Dislikes: 983
# Total Accepted:    2.9M
# Total Submissions: 5M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome or
# false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,2,1]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
# 
# 
# 
# Follow up: Could you do it in O(n) time and O(1) space?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # slow 慢指针，fast 快指针
        # fast 从 head.next 开始，是为了让 slow 最后停在前半段的最后一个节点
        slow, fast = head, head.next

        # 快慢指针找链表中点
        # fast 每次走两步，slow 每次走一步
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 从 slow.next 开始反转后半段链表
        # pre 最后会指向反转后后半段的头节点
        pre, curr = None, slow.next

        while curr:
            # 先保存 curr 的下一个节点，避免反转指针后丢失后面的链表
            nxt = curr.next

            # 反转当前节点的 next 指针
            curr.next = pre

            # pre 和 curr 同时向后移动
            pre = curr
            curr = nxt

        # 此时：
        # head 指向前半段开头
        # pre 指向反转后的后半段开头
        # 逐个比较前半段和后半段的节点值
        while pre:
            # 只要有一个值不同，就不是回文链表
            if pre.val != head.val:
                return False

            # 两个指针同时向后移动
            pre = pre.next
            head = head.next

        # 如果后半段全部比较完都相同，说明是回文链表
        return True
        
# @lc code=end

