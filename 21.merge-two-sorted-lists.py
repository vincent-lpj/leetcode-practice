#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 链表（linked list）是一种常用的数据结构，由一系列的节点组成
        # 每个节点包含数据域和指针域
        # 指针域存储了下一个节点的地址
        # Python中通过类来表示链表节点

        # 创建一个虚拟头节点 dummy
        # 作用：方便统一处理链表头部，避免单独判断第一个节点
        dummy = ListNode()

        # curr 指针用于构建新的合并链表
        # 一开始指向 dummy，之后不断向后移动
        curr = dummy
        
        # 当两个链表都还有节点时，比较当前节点的值
        while list1 and list2:
            # 如果 list1 当前节点的值更小或相等
            # 就把 list1 当前节点接到 curr 后面
            if list1.val <= list2.val:
                curr.next = list1

                # list1 指针向后移动一位
                # 注意：必须赋值，否则 list1 不会真的移动
                list1 = list1.next
            else:
                # 否则，把 list2 当前节点接到 curr 后面
                curr.next = list2

                # list2 指针向后移动一位
                list2 = list2.next

            # curr 指针向后移动一位
            # 指向刚刚接入的新节点
            curr = curr.next

        # 跳出循环后，说明至少有一个链表已经遍历完
        # 由于两个链表本身都是有序的，所以剩下的部分可以直接接到 curr 后面
        curr.next = list1 or list2

        # dummy 是虚拟头节点，不属于真正结果
        # 真正合并后的链表从 dummy.next 开始
        return dummy.next
        
# @lc code=end

