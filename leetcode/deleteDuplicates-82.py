#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        while head is None:
            return head
        res_list = []
        current = head
        while current:
            res_list.append(current.val)
            current = current.next
        nums_dict = OrderedDict()
        for i in res_list:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
        res_list_rd = [key for (key, value) in nums_dict.items() if value == 1]
        res = ListNode(0)
        current = res
        for i in res_list_rd:
            current.next = ListNode(i)
            current = current.next
        return res.next


class Solution2:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        c_res = res
        current = head
        front = float('inf')
        while current:
            if current.val != front:
                if current.next:
                    if current.val != current.next.val:
                        c_res.next = ListNode(current.val)
                        c_res = c_res.next
                else:
                    c_res.next = current
            front = current.val
            current = current.next

        return res.next
