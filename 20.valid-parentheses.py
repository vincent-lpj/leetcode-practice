#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 用字典保存每个左括号对应的右括号
        pairs_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        # stack 用来保存还没有匹配的左括号
        stack = []

        # 遍历字符串中的每一个括号
        for char in s:
            # 如果当前字符是左括号，就放入栈中
            if char in pairs_dict:
                stack.append(char)
            else:
                # 如果当前字符是右括号，但栈为空
                # 说明没有对应的左括号，直接返回 False
                if not stack:
                    return False

                # 取出最近的一个左括号
                left = stack.pop()

                # 判断这个左括号对应的右括号是否等于当前字符
                # 例如 left = '('，那么 pairs_dict[left] 应该是 ')'
                if pairs_dict[left] != char:
                    return False

        # 最后如果 stack 为空，说明所有左括号都被正确匹配了
        # 如果 stack 不为空，说明还有左括号没有匹配
        return not stack

        
# @lc code=end

