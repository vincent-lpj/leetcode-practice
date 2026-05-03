#
# @lc app=leetcode id=908 lang=python3
#
# [908] Smallest Range I
#
# https://leetcode.com/problems/smallest-range-i/description/
#
# algorithms
# Easy (73.49%)
# Likes:    796
# Dislikes: 2089
# Total Accepted:    125.7K
# Total Submissions: 171.1K
# Testcase Example:  '[1]\n0'
#
# You are given an integer array nums and an integer k.
# 
# In one operation, you can choose any index i where 0 <= i < nums.length and
# change nums[i] to nums[i] + x where x is an integer from the range [-k, k].
# You can apply this operation at most once for each index i.
# 
# The score of nums is the difference between the maximum and minimum elements
# in nums.
# 
# Return the minimum score of nums after applying the mentioned operation at
# most once for each index in it.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1], k = 0
# Output: 0
# Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,10], k = 2
# Output: 6
# Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8
# - 2 = 6.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,3,6], k = 3
# Output: 0
# Explanation: Change nums to be [4, 4, 4]. The score is max(nums) - min(nums)
# = 4 - 4 = 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^4
# 0 <= k <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # 原数组中的最大值和最小值
        mx, mi = max(nums), min(nums)
        
        # 最大值最多可以减小 k，最小值最多可以增大 k
        # 所以最大差值最多可以缩小 2 * k
        #
        # 如果 mx - mi <= 2 * k，说明所有数可以调整到有重叠的范围内，
        # 最小 score 可以变成 0
        #
        # 否则，最小 score 就是原差值减去 2 * k
        return max(0, mx - mi - k * 2)
# @lc code=end

