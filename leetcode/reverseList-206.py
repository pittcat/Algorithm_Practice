#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
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

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res_list = self.linklist2list(head)
        res_list.reverse()
        first = ListNode(0)
        cur = first
        for i in res_list:
            cur.next = ListNode(i)
            cur = cur.next
        return first.next


class Solution2:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev
