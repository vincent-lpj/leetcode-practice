#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        y = 0

        for i in range(len(s)):
            # 如果是最后一个字符，直接加
            # 如果当前字符大于或等于右边字符，说明是正常情况，也加
            if i == len(s) - 1 or roman_dict[s[i]] >= roman_dict[s[i + 1]]:
                y += roman_dict[s[i]]
            # 如果当前字符小于右边字符，说明是特殊情况，需要减
            # 这道题最关键的是找出三种特殊值的规律，也就是左边出现的字母代表的数字比右一位小
            # 例如 IV = 5 - 1，IX = 10 - 1
            else:
                y -= roman_dict[s[i]]

        return y
        
# @lc code=end

