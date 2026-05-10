#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (81.87%)
# Likes:    20900
# Dislikes: 385
# Total Accepted:    3.1M
# Total Submissions: 3.8M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# 
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 解法 1：递归传参，不回溯 pop
        # result = []

        # def dfs(remaining: List[int], path: List[int]):
        #     """
        #     remaining: 当前还没有被使用的数字
        #     path: 当前已经构造出来的排列
        #     """

        #     # 如果没有剩余数字了，说明 path 已经是一个完整排列
        #     if not remaining:
        #         result.append(path)
        #         return

        #     # 枚举当前剩余数字中的每一个数
        #     for i, num in enumerate(remaining):
        #         # 生成新的剩余数字列表：
        #         # 去掉当前选择的 remaining[i]
        #         new_remaining = remaining[:i] + remaining[i + 1:]

        #         # 生成新的路径：
        #         # 在当前 path 后面加上 num
        #         # 注意这里创建了新列表，所以递归回来后不需要 pop
        #         dfs(new_remaining, path + [num])

        # # 一开始所有数字都还没使用，当前路径为空
        # dfs(nums, [])

        # return result

        # 解法 2：用剩余列表 lst + 回溯
        # results = []
        # path = []

        # def dfs(lst):
        #     # 如果当前路径长度等于 nums 长度，说明已经形成一个完整排列
        #     if len(path) == len(nums):
        #         results.append(path[:])
        #         return

        #     # 遍历当前还没有被选择的数字
        #     for num in lst:
        #         # 选择当前数字
        #         path.append(num)

        #         # 构造下一层递归可选的数字列表
        #         nxt_lst = lst[:]
        #         nxt_lst.remove(num)

        #         # 继续递归
        #         dfs(nxt_lst)

        #         # 回溯，撤销选择
        #         path.pop()

        # dfs(nums)
        # return results

        # 解法 3：用 path 判断是否已经使用过
        result = []
        path = []

        def dfs():
            # path 长度等于 nums 长度，说明已经构造出一个完整排列
            if len(path) == len(nums):
                result.append(path[:])  # 注意要拷贝一份
                return

            # 每一层都尝试选择 nums 中还没出现在 path 里的数字
            for num in nums:
                # 如果 num 已经在当前 path 中，说明这个排列分支已经用过它
                if num in path:
                    continue

                # 选择当前数字
                path.append(num)

                # 继续递归构造下一个位置
                dfs()

                # 回溯：撤销刚才的选择
                # 因为 path 是同一个列表对象，所以递归回来后必须 pop
                path.pop()

        dfs()
        return result
# @lc code=end

