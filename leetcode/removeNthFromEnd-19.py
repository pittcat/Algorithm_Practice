#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return head
        res_list = []
        current = head
        while current:
            res_list.append(current.val)
            current = current.next
        l = len(res_list)
        del_idx = l - n
        first = ListNode(0)
        c_fist = first
        for i in range(len(res_list)):
            if i == del_idx:
                continue
            c_fist.next = ListNode(res_list[i])
            c_fist = c_fist.next

        return first.next
