#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 以第一个字符串作为基准，逐个字符检查
        # 例如 strs = ["flower", "flow", "flight"]
        # 就先检查所有字符串的第 0 位，再检查第 1 位，以此类推

        for i in range(len(strs[0])):
            # 遍历数组中的每一个字符串，检查它们第 i 位是否一致
            for s in strs:
                # 如果当前字符串长度不够，说明公共前缀到这里结束
                # 例如 strs[0] = "flower", s = "flow"
                # 当 i = 4 时，s 已经没有第 4 位了
                #
                # 或者当前字符串第 i 位和 strs[0] 第 i 位不同
                # 说明公共前缀也到这里结束
                if len(s) <= i or s[i] != strs[0][i]:
                    # 返回从开头到 i 之前的部分
                    # 注意这里不包含第 i 位，因为第 i 位已经不匹配了
                    return s[:i]

        # 如果第一个字符串全部检查完都没有发现不匹配
        # 说明第一个字符串本身就是最长公共前缀
        # 例如 ["flow", "flower", "flight"] 中，最多只能返回 "fl"
        # 但如果是 ["flow", "flower", "flow"]，检查完 "flow" 后就返回 "flow"
        return strs[0]
        
# @lc code=end

