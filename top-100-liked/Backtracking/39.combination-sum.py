#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (76.45%)
# Likes:    21025
# Dislikes: 542
# Total Accepted:    3.1M
# Total Submissions: 4.1M
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.
# 
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.
# 
# The test cases are generated such that the number of unique combinations that
# sum up to target is less than 150 combinations for the given input.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# 
# 
# Example 3:
# 
# 
# Input: candidates = [2], target = 1
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 先排序，方便后面剪枝
        candidates.sort()

        result = []
        path = []

        def dfs(start: int, remaining: int):
            """
            start: 当前可以从 candidates[start] 开始选，避免重复组合
            remaining: 当前还需要凑出的目标值
            path: 当前已经选择的数字组合
            """

            # 剩余目标值为 0，说明当前 path 正好凑出了 target
            if remaining == 0:
                result.append(path[:])
                return

            # 从 start 开始选，保证组合不会倒退，避免重复排列
            for index in range(start, len(candidates)):
                num = candidates[index]

                # 因为 candidates 已经排序
                # 如果当前 num 已经大于 remaining，后面的数也更大，不可能成功
                if num > remaining:
                    break

                # 选择当前数字
                path.append(num)

                # 继续搜索
                # 这里传 index，而不是 index + 1
                # 因为同一个数字可以被重复使用
                dfs(index, remaining - num)

                # 撤销选择，回到上一层，尝试下一个数字
                path.pop()

        dfs(0, target)
        return result
                
# @lc code=end

