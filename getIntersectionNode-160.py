#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def length(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        return length

    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        A_length = self.length(headA)
        B_length = self.length(headB)
        disdance = abs(A_length - B_length)
        cur_a = headA
        cur_b = headB
        if A_length > B_length:
            for i in range(disdance):
                cur_a = cur_a.next
        elif A_length < B_length:
            for i in range(disdance):
                cur_b = cur_b.next
        while cur_a:
            if cur_a.val == cur_b.val:
                return cur_a
            cur_a = cur_a.next
            cur_b = cur_b.next
        return None
