#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (65.95%)
# Likes:    21012
# Dislikes: 1137
# Total Accepted:    3M
# Total Submissions: 4.6M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
# 
# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# Example 1:
# 
# 
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# 
# Example 2:
# 
# 
# Input: digits = "2"
# Output: ["a","b","c"]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
# 
# 
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # # 如果输入为空，直接返回空列表
        # if not digits:
        #     return []

        # # 下标 0 对应数字 2，下标 1 对应数字 3，以此类推
        # d = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        # # ans 保存当前已经生成的组合
        # # 初始为空字符串，方便后面拼接第一个数字对应的字母
        # ans = [""]

        # # 逐个处理 digits 中的每个数字
        # for i in digits:
        #     # 找到当前数字对应的字母字符串
        #     # 比如 i = "2"，int(i) - 2 = 0，对应 "abc"
        #     s = d[int(i) - 2]

        #     # 将已有组合 a 和当前数字对应的每个字母 b 进行拼接
        #     # 相当于在每个旧组合后面追加一个新字母
        #     ans = [a + b for a in ans for b in s]

        # # 返回所有组合
        # return ans

        # 递归解法：
        # 如果输入为空，直接返回空列表
        if not digits:
            return []

        # 数字到字母的映射
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def dfs(index: int, path: str):
            """
            index: 当前正在处理 digits 的第几个数字
            path: 当前已经拼出来的字母组合
            """

            # 如果 index 走到 digits 末尾，
            # 说明已经为每个数字都选好了一个字母
            if index == len(digits):
                result.append(path)
                return

            # 当前要处理的数字
            digit = digits[index]

            # 遍历当前数字对应的所有字母
            for ch in phone[digit]:
                # 选择一个字母 ch，拼到 path 后面
                # 然后递归处理下一个数字
                dfs(index + 1, path + ch)

        # 从第 0 个数字开始搜索，初始组合为空字符串
        dfs(0, "")

        return result
        
# @lc code=end

