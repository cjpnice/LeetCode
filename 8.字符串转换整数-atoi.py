#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start



class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 死去吧
        # numStr = ''
        # num = 0
        # first = ''
        # for str in s:
        #     if str == ' ' and first == '':
        #         continue
        #     if first == '' and str == '-':
        #         first = '-'
        #         continue
        #     if first == '' and str not in ".1234567890":
        #         first = '+'
        #         continue
        #     if (numStr != '' or first != '') and str not in ".1234567890":
        #         break
        #     elif numStr == '' and str not in ".1234567890":
        #         continue
        #     else:
        #         if first == '':
        #             first = str
        #         numStr += str
        # if first == '-' and numStr != '':
        #     num = -int(float(numStr))
        # elif numStr != '':
        #     num = int(float(numStr))
        # else:
        #     num = 0
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)
        # return num

# @lc code=end

# if __name__ == "__main__":
#   solution = Solution()
#   solution.myAtoi("b11228552307")