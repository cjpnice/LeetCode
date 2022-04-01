#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode() # 输出
        result_p = result 
        if l1 == None: return l2
        if l2 == None: return l1
        carry = 0 # 进位
        # 当l1和l2都有值时，计算l1,l2和进位的和，并更新进位
        while l1 and l2:
            sum = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            result_p.next = ListNode(sum)
            result_p = result_p.next
            l1 = l1.next
            l2 = l2.next
        # 当l1还有值l2没有值得时候，将l1的值和进位相加，并更新进位
        if l1:
            while l1:
                sum = (l1.val + carry) % 10
                carry = (l1.val + carry) // 10
                result_p.next = ListNode(sum)
                result_p = result_p.next
                l1 = l1.next

        # 当l2还有值l1没有值得时候，将l2的值和进位相加，并更新进位
        if l2:
            while l2:
                sum = (l2.val + carry) % 10
                carry = (l2.val + carry) // 10
                result_p.next = ListNode(sum)
                result_p = result_p.next
                l2 = l2.next
        # 当l1和l2都没有值时，如果进位还有则加到结果中
        if carry != 0:
            result_p.next = ListNode(carry)
            result_p = result_p.next
        return result.next


# if __name__ == "__main__":

#     l1 = ListNode(2,ListNode(4))
#     l2 = ListNode(5,ListNode(6,ListNode(4)))
#     solution = Solution()
#     result = solution.addTwoNumbers(l1,l2)

# @lc code=end

