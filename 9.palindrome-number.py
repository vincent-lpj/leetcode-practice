#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 回文数的数学解法：不把整数转成字符串，只反转数字的后一半

        # 负数不是回文数，因为反转后负号位置不一样
        # 例如：-121 反转后类似 121-
        #
        # 如果 x 不为 0 且最后一位是 0，也不是回文数
        # 因为回文数的第一位也必须是 0，但整数不会以 0 开头
        # 例如：10、100、120 都不是回文数
        if x < 0 or (x and x % 10 == 0):
            return False

        # reversed_half 用来保存 x 后半部分反转后的结果
        # 例如 x = 1221 时，后半部分 21 反转后会变成 12
        reversed_half = 0

        # 每次从 x 的末尾取出一位，加入到 reversed_half 后面
        # 同时把 x 的最后一位去掉
        #
        # 当 reversed_half >= x 时，说明已经处理了大约一半的数字
        while reversed_half < x:
            # x % 10 取出 x 的最后一位
            # reversed_half * 10 把当前 reversed_half 左移一位
            # 然后加上取出的最后一位
            reversed_half = reversed_half * 10 + x % 10

            # 去掉 x 的最后一位
            x //= 10

        # 如果原数字长度是偶数：
        # 例如 1221，循环结束后 x = 12, reversed_half = 12
        # 此时 x == reversed_half
        #
        # 如果原数字长度是奇数：
        # 例如 12321，循环结束后 x = 12, reversed_half = 123
        # 中间的数字 3 不影响回文判断，所以用 reversed_half // 10 去掉它
        #
        # 只要满足其中一种情况，就是回文数
        return x == reversed_half or x == reversed_half // 10
# @lc code=end

