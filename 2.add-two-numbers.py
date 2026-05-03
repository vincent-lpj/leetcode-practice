#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (48.37%)
# Likes:    36809
# Dislikes: 7263
# Total Accepted:    7M
# Total Submissions: 14.5M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# 
# Example 2:
# 
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建虚拟头节点，方便拼接结果链表
        dummy = ListNode()

        # carry 表示进位，curr 用来构建结果链表
        carry, curr = 0, dummy

        # 只要 l1、l2 还有节点，或者还有进位，就继续计算
        while l1 or l2 or carry:
            # 当前位的和 =
            # l1 当前位 + l2 当前位 + 上一位进位
            # 如果某个链表已经走完，就把它当前位当作 0
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

            # divmod(s, 10) 同时得到进位和当前位数字
            # carry = s // 10
            # val = s % 10
            carry, val = divmod(s, 10)

            # 用当前位数字创建新节点，接到结果链表后面
            curr.next = ListNode(val)

            # curr 后移，准备接下一个结果节点
            curr = curr.next

            # l1 和 l2 各自后移一位
            # 如果已经为空，就继续保持 None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # dummy.next 是结果链表的真正头节点
        return dummy.next

# @lc code=end

