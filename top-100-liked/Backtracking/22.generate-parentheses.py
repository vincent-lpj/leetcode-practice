#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (78.60%)
# Likes:    23311
# Dislikes: 1086
# Total Accepted:    2.9M
# Total Submissions: 3.7M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # result 用来保存所有合法的括号组合
        result = []

        def dfs(left_count: int, right_count: int, path: str):
            """
            left_count: 当前已经使用的左括号数量
            right_count: 当前已经使用的右括号数量
            path: 当前已经构造出来的括号字符串
            """

            # 情况 1：左括号用多了，不合法，停止这一条递归分支
            if left_count > n:
                return

            # 情况 2：右括号用多了，不合法，停止这一条递归分支
            if right_count > n:
                return

            # 情况 3：右括号数量超过左括号数量，不合法
            # 因为右括号必须匹配前面已经出现的左括号
            # 例如 ")("、"())" 这种前缀都不可能变成合法括号
            if right_count > left_count:
                return

            # 如果左右括号都刚好用了 n 个，
            # 说明 path 已经是一个完整且合法的括号组合
            if left_count == n and right_count == n:
                result.append(path)
                return

            # 选择 1：尝试在当前 path 后面加一个左括号
            # 加完后，left_count 增加 1
            dfs(left_count + 1, right_count, path + "(")

            # 选择 2：尝试在当前 path 后面加一个右括号
            # 加完后，right_count 增加 1
            dfs(left_count, right_count + 1, path + ")")

        # 从空字符串开始搜索
        # 一开始左括号和右括号都用了 0 个
        dfs(0, 0, "")

        return result

# @lc code=end

