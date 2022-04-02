#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
import re


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # ------该方法超时-----------------------------
        # maxLen = 0
        # longestPalindrome = ""
        # sLen = len(s)
        # for i in range(sLen+1):
        #     for ii in range(i+1, sLen+1):
        #         palindromeLen = self.isPalindrome(s[i:ii])
        #         if palindromeLen > maxLen:
        #             maxLen = palindromeLen
        #             longestPalindrome = s[i:ii]

        # return longestPalindrome
        #----------------------------------------------
        n = len(s)
        if n < 2:
            return s
        
        max_len = 1
        begin = 0
        # 使用二维数组dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break
                    
                if s[i] != s[j]:
                    dp[i][j] = False 
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]


    
    def isPalindrome(self, s):
        sLen = len(s)
        for i in range(sLen):
            if i + 1 <= sLen-1-i:
                if s[i] != s[sLen-1-i]:
                    return 0
            else:
                break
        return sLen

if __name__ == "__main__":
    solution = Solution()
    solution.longestPalindrome("babad")

# @lc code=end

