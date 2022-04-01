#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = []
        nums1_p = 0
        nums2_p = 0
        nums1Len = len(nums1)
        nums2Len = len(nums2)
        # 使用两个指针向后遍历两个列表，将小的放入num列表中，指针向后移直到其中一个遍历结束
        while nums1_p < nums1Len and nums2_p < nums2Len:
            if nums1[nums1_p] <= nums2[nums2_p]:
                num.append(nums1[nums1_p])
                nums1_p += 1
            else:
                num.append(nums2[nums2_p])
                nums2_p += 1
        # 将剩余的列表加入num列表中
        if nums1_p == nums1Len:
            while nums2_p < nums2Len:
                num.append(nums2[nums2_p])
                nums2_p += 1
        else:
            while nums1_p < nums1Len:
                num.append(nums1[nums1_p])
                nums1_p += 1
        # 计算中位数
        if (nums1Len + nums2Len) % 2 == 0:
            return (num[int((nums1Len + nums2Len)/2-1)] + num[int((nums1Len + nums2Len)/2)]) / 2.0
        else:
            return num[int((nums1Len + nums2Len - 1) / 2)]

            
# if __name__ == "__main__":
#     solution = Solution()
#     res = solution.findMedianSortedArrays([1,2],[3,4])
#     s =0
            

# @lc code=end

