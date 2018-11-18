#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        cur = head
        res_lst = []
        res_node = ListNode(1)
        res_cur = res_node
        while cur:
            res_lst.append(cur.val)
            cur = cur.next
        k = k % len(res_lst)
        res_lst = res_lst[-k:] + res_lst[:-k]
        for i in res_lst:
            res_cur.next = ListNode(i)
            res_cur = res_cur.next
        return res_node.next
