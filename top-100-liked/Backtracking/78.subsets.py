#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (82.28%)
# Likes:    19260
# Dislikes: 341
# Total Accepted:    3M
# Total Submissions: 3.7M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# 
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def dfs(index: int):
            # base case：
            # index 走到 nums 末尾，说明每个元素都已经决定完“选或不选”
            # 当前 path 就是一个完整子集
            if index == len(nums):
                result.append(path[:])
                return

            # Subsets 的递归展开方式：
            # 每一层固定处理 nums[index] 这个元素，
            # 对它只有两个选择：
            # 1. 不选 nums[index]
            # 2. 选 nums[index]
            #
            # 所以这是“选 / 不选”的二叉递归结构，
            # 不是像全排列/组合总和那样用 for 在多个候选里选一个。

            # 选择 1：不选 nums[index]，直接处理下一个元素
            dfs(index + 1)

            # 选择 2：选 nums[index]
            path.append(nums[index])
            dfs(index + 1)

            # 回溯：撤销选择，恢复现场
            path.pop()

        dfs(0)
        return result
# @lc code=end

