#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
import re


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        if x < 0:
            # 当x小于0时，先转换为正数
            x = -x
            while x != 0:
                # 取出x的最后一位
                digit = x % 10
                # 减去最后一位
                x = (x - digit) // 10
                # 计算翻转的数
                rev  = rev * 10 + digit
            rev = -rev
        else:
            # 大于0时，同上
            while x != 0:
                digit = x % 10
                x = (x - digit) // 10
                rev  = rev * 10 + digit
        # 判断翻转后的数字是否越界
        if rev > 2**31 - 1 or rev < -2**31:
            rev = 0 
        return rev



# @lc code=end

# if __name__ == "__main__":
#     solution = Solution()
#     solution.reverse(123)
