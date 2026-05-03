#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#
# https://leetcode.com/problems/toeplitz-matrix/description/
#
# algorithms
# Easy (69.68%)
# Likes:    3734
# Dislikes: 181
# Total Accepted:    455K
# Total Submissions: 653K
# Testcase Example:  '[[1,2,3,4],[5,1,2,3],[9,5,1,2]]'
#
# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise,
# return false.
# 
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the
# same elements.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,2],[2,2]]
# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 20
# 0 <= matrix[i][j] <= 99
# 
# 
# 
# Follow up:
# 
# 
# What if the matrix is stored on disk, and the memory is limited such that you
# can only load at most one row of the matrix into the memory at once?
# What if the matrix is so large that you can only load up a partial row into
# the memory at once?
# 
# 
#

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])

        # 核心思路：
        # 不用逐条比较整条对角线，只需要比较每个元素和它右下角的元素。
        # 如果所有 matrix[row][col] == matrix[row + 1][col + 1]，
        # 那么每条左上到右下的对角线都相等。
        #
        # 边界：
        # 最后一行没有 row + 1，最后一列没有 col + 1，
        # 所以只遍历到 m - 1 和 n - 1 之前。
        for row in range(m - 1):
            for col in range(n - 1):
                if matrix[row][col] != matrix[row + 1][col + 1]:
                    return False

        return True
# @lc code=end

