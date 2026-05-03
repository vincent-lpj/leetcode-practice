#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (63.63%)
# Likes:    16652
# Dislikes: 1500
# Total Accepted:    2.4M
# Total Submissions: 3.7M
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3'
#
# Given the heads of two singly linked-lists headA and headB, return the node
# at which the two lists intersect. If the two linked lists have no
# intersection at all, return null.
# 
# For example, the following two linked lists begin to intersect at node c1:
# 
# The test cases are generated such that there are no cycles anywhere in the
# entire linked structure.
# 
# Note that the linked lists must retain their original structure after the
# function returns.
# 
# Custom Judge:
# 
# The inputs to the judge are given as follows (your program is not given these
# inputs):
# 
# 
# intersectVal - The value of the node where the intersection occurs. This is 0
# if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head)
# to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head)
# to get to the intersected node.
# 
# 
# The judge will then create the linked structure based on these inputs and
# pass the two heads, headA and headB to your program. If you correctly return
# the intersected node, then your solution will be accepted.
# 
# 
# Example 1:
# 
# 
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA =
# 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0
# if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as
# [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are
# 3 nodes before the intersected node in B.
# - Note that the intersected node's value is not 1 because the nodes with
# value 1 in A and B (2^nd node in A and 3^rd node in B) are different node
# references. In other words, they point to two different locations in memory,
# while the nodes with value 8 in A and B (3^rd node in A and 4^th node in B)
# point to the same location in memory.
# 
# 
# Example 2:
# 
# 
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3,
# skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2 (note that this must not be 0
# if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as
# [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node
# before the intersected node in B.
# 
# 
# Example 3:
# 
# 
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
# Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it
# reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0,
# while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes of listA is in the m.
# The number of nodes of listB is in the n.
# 1 <= m, n <= 3 * 10^4
# 1 <= Node.val <= 10^5
# 0 <= skipA <= m
# 0 <= skipB <= n
# intersectVal is 0 if listA and listB do not intersect.
# intersectVal == listA[skipA] == listB[skipB] if listA and listB
# intersect.
# 
# 
# 
# Follow up: Could you write a solution that runs in O(m + n) time and use only
# O(1) memory?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # # 哈希表解
        # # 创建一个 set，用来记录 A 链表中出现过的节点对象
        # visited = set()

        # # 先遍历 A 链表
        # p = headA
        # while p:
        #     # 把当前节点对象加入 set
        #     # 注意：这里存的是节点本身，不是节点的值 p.val
        #     visited.add(p)

        #     # 指针后移，继续访问下一个节点
        #     p = p.next

        # # 再遍历 B 链表
        # q = headB
        # while q:
        #     # 如果当前 B 节点已经出现在 A 的节点集合中
        #     # 说明 A 和 B 从这个节点开始相交
        #     if q in visited:
        #         return q

        #     # 指针后移，继续检查下一个节点
        #     q = q.next

        # # 如果 B 遍历结束都没有找到相同节点，说明两个链表不相交
        # return None
    
        # 双指针：a 走 A+B，b 走 B+A，用交换链表头来抵消长度差
        a, b = headA, headB

        while a != b:
            # a 走完 A 后去走 B
            a = a.next if a else headB

            # b 走完 B 后去走 A
            b = b.next if b else headA

        # 相交则返回交点；不相交则返回 None
        return a
        

# @lc code=end

