#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
from operator import index


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1, num1 in enumerate(nums):
            # 循环遍历nums,用target减去当前遍历的数得到差值,
            # 再遍历后面的数判断是否存在该差值，存在说明两数相加为target，
            # 返回两数下标
            diff = target - num1
            for index2, num2 in enumerate(nums[index1+1:]):
                if diff == num2:
                    return [index1, index2+index1+1]
            
# @lc code=end

