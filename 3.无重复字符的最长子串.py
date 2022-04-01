#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start




class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        # 如果输出字符串长度为0或者1直接返回字符串长度
        if len(s)==1 or len(s)==0:
            return len(s)
        # 两个指针i和ii,i从字符串第一个开始，ii从i后面一个开始，判断ii位置上的字符是否在i-ii上出现，如果出现就判断是否为最大长度
        # i继续向前进一位重复上面判断，找出最大长度 
        for i in range(len(s)):
            for ii in range(i + 1, len(s)):
                if s[ii] in s[i:ii]:
                    if ii - i > maxLen:
                        maxLen = ii - i
                    break
                # 如果ii遍历到最后一位都没有重复的字符，
                # 则计算此时的长度
                if ii == len(s)-1:
                    if ii - i + 1 > maxLen:
                        maxLen = ii - i + 1
        return maxLen


# if __name__ == "__main__":
#     solution = Solution()
#     solution.lengthOfLongestSubstring("pwwkew")

# @lc code=end

