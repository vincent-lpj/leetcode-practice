#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (73.97%)
# Likes:    14308
# Dislikes: 573
# Total Accepted:    1.3M
# Total Submissions: 1.8M
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.
# 
# 
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 16
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # res 用来存放所有合法的回文分割方案
        res = []

        # path 用来存放当前正在构造的一组分割结果
        path = []

        def dfs(index):
            # 如果 index 走到了字符串末尾，说明当前 path 是一种完整的分割方案
            if index == len(s):
                # 注意这里要拷贝一份 path，因为后续回溯还会修改 path
                res.append(path[:])
                return

            # 枚举从 index 开始的所有子串结束位置
            # end 是切片右边界，不包含 end
            for end in range(index + 1, len(s) + 1):
                # 取出当前要判断的子串
                substring = s[index:end]

                # 判断当前子串是否是回文串
                # substring[::-1] 表示反转后的字符串
                if substring == substring[::-1]:
                    # 如果是回文串，就加入当前路径
                    path.append(substring)

                    # 继续从 end 位置开始切割剩下的字符串
                    dfs(end)

                    # 回溯：撤销刚才的选择，尝试其他切割方式
                    path.pop()

        # 从字符串的第 0 个位置开始搜索
        dfs(0)

        # 返回所有回文分割方案
        return res

# @lc code=end

