#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr 指向当前正在检查的节点
        curr = head

        # 只有当前节点和下一个节点都存在时，才需要继续比较
        while curr and curr.next:
            # 因为链表已经排序，重复的元素一定相邻
            # 如果当前节点的值和下一个节点的值相同，就跳过下一个节点
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                # 如果不重复，当前节点向后移动一位
                curr = curr.next

        # 返回去重后的链表头节点
        return head

# @lc code=end

