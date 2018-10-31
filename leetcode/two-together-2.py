#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l1: ListNode
        :rtype: ListNode
        """

        List1, List2 = [], []
        while l1.next is not None:
            List1.append(l1.val)
            l1 = l1.next
        List1.append(l1.val)
        while l2.next is not None:
            List2.append(l2.val)
            l2 = l2.next
        List2.append(l2.val)
        List1.reverse()
        List2.reverse()
        num1str = ''
        num2str = ''
        for i in List1:
            num1str += str(i)
        for i in List2:
            num2str += str(i)
        result_number = int(num1str) + int(num2str)
        result_list = list(str(result_number))
        __import__('ipdb').set_trace()
        result_list.reverse()
        result = ListNode(int(result_list[0]))
        current = result
        for i in result_list[1:]:
            run_res = ListNode(int(i))
            current.next = run_res
            current = run_res
        return result


#  lst1 = [2, 4, 3]
#  lst2 = [5, 6, 4]

#  l1 = ListNode(lst1[0])
#  l2 = ListNode(lst2[0])
#  current_lst1 = l1
#  current_lst2 = l2
#  for i in lst1[1:]:
    #  run_l1 = ListNode(i)
    #  current_lst1.next = run_l1
    #  current_lst1 = run_l1
#  for i in lst2[1:]:
    #  run_l2 = ListNode(i)
    #  current_lst2.next = run_l2
    #  current_lst2 = run_l2
#  moe = Solution()
#  moe_rst = moe.addTwoNumbers(l1, l2)
