#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def linklist2list(self, l):
        """
        :type l: ListNode
        :rtype: list
        """
        current = l
        res = []
        while current:
            res.append(current.val)
            current = current.next
        return res

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not (l1 and l2):
            return l1 or l2
        res = str(
            int(''.join([str(i) for i in self.linklist2list(l1)])) +
            int(''.join([str(i) for i in self.linklist2list(l2)])))
        head = ListNode(0)
        cur = head
        for i in res:
            cur.next = ListNode(int(i))
            cur = cur.next
        return head.next
