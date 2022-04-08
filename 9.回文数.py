#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start



class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        sLen = len(s)
        # 从头和尾同时开始判断是否相同
        for i in range(sLen):
            if i + 1 <= sLen-1-i:
                if s[i] != s[sLen-1-i]:
                    return False
            else:
                break
        return True

     
# @lc code=end

