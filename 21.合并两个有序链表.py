#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode() 
        result_p = result 
        # 两个指针遍历连链表，将小的数据放入result链表中，直到有一个链表全部放完，
        # 最后将另一个链表直接加到result链表后
        while list1 and list2:
            if list1.val <= list2.val:
                result_p.next = ListNode(list1.val)
                result_p = result_p.next
                list1 = list1.next
            else:
                result_p.next = ListNode(list2.val)
                result_p = result_p.next
                list2 = list2.next
        if list1:
            result_p.next = list1
        if list2:
            result_p.next = list2
        return result.next
# @lc code=end

# if __name__ == "__main__":
#   solution = Solution()
#   l1 = ListNode(1,ListNode(2))
#   l2 = ListNode(1,ListNode(3,ListNode(4)))
#   solution.mergeTwoLists(l1, l2)