#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 实现 strStr()
#

# @lc code=start



class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        index = []
        # 遍历haystack，找出所有和needle第一个字符串相同的坐标，存入一个数组中
        for i, str in enumerate(haystack):
            if str == needle[0]:
                index.append(i)
        # 遍历该数组，判断从该位置开始后面是否也相同，相同则返回当前位置
        for i in index:
            if needle == haystack[i:len(needle)+i]:
                return i
        return -1

# @lc code=end

# if __name__ == "__main__":
#   solution = Solution()
#   haystack = "hello"
#   needle = "ll"
#   solution.strStr(haystack, needle)