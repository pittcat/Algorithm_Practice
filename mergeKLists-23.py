#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        first = ListNode(0)
        ele = []
        for i in lists:
            while i:
                ele.append(i.val)
                i = i.next
        cur = first
        for i in sorted(ele):
            cur.next = ListNode(i)
            cur = cur.next
        return first.next
