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
        res = []
        path = []
        def dfs(index):
            if index == len(s):
                res.append(path[:])
                return

            for end in range(index + 1, len(s) + 1):
                substring = s[index:end]

                if substring == substring[::-1]:
                    path.append(substring)
                    dfs(end)
                    path.pop()

        dfs(0)
        return res

# @lc code=end

