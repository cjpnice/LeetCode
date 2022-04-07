#
# @lc app=leetcode.cn id=6 lang=python
#
# [6] Z 字形变换
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2: return s
        # res存储每一行的字符
        res = ["" for _ in range(numRows)]
        # i代表行数， flag代表是加行数的移动方向，是加还是减
        i, flag = 0, -1
        for c in s:
            res[i] += c
            # 当行数是第一行或者最后一行就翻转flag,使行数i在0~numRows - 1之间上下移动
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        # 最后将每一行拼接返回
        return "".join(res)
                


# if __name__ == "__main__":
#     solution = Solution()
#     solution.convert("LEETCOD", 3)
# @lc code=end

