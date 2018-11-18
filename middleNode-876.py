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

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nums = self.linklist2list(head)
        mid_idx = len(nums) // 2 + 1
        count = 1
        current = head
        while current:
            if count == mid_idx:
                break
            current = current.next
            count += 1

        return current
