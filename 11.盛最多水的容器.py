#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 使用双指针，从头和尾开始扫描，计算两个指针之间的容积，判断是否为当前最大容积，
        # 再将指针从较小的一端移动，重复上述计算，直到头指针大于尾指针
        i = 0
        j = len(height)-1
        tempArea = 0
        maxArea = 0
        while i < j:
          if height[i] <= height[j]:
            tempArea = height[i] * (j - i)
            i += 1
          else:
            tempArea = height[j] * (j - i)
            j -= 1
          if tempArea > maxArea:
            maxArea = tempArea
        return maxArea



# @lc code=end

if __name__ == "__main__":
  solution = Solution()
  solution.maxArea([1,8,6,2,5,4,8,3,7])