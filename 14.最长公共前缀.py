#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start



class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 如果列表中存在"",则直接返回""
        if "" in strs:
            return ""
        # 循环遍历列表中的字符，并从头开始比较每个字符串是否一致，不一致就返回当前匹配的公共前缀
        for i in range(len(strs[0])):
            currentStr = strs[0][i]
            for str in strs:
                # 当列表中的第一个字符串长度超过后面的字符串时，返回最短字符串
                if i >= len(str):
                    return strs[0][0:i]
                if currentStr != str[i]:
                    return strs[0][0:i]
        return strs[0][0:len(strs[0])]

              


# @lc code=end

if __name__ == "__main__":
  solution = Solution()
  solution.longestCommonPrefix(["ab", "a"])