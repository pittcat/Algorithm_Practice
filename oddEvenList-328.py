#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = ListNode(0)
        even = ListNode(1)
        cur = head
        odd_cur = odd
        even_cur = even
        polar = True
        while cur:
            if polar:
                odd_cur.next = ListNode(cur.val)
                odd_cur = odd_cur.next
            else:
                even_cur.next = ListNode(cur.val)
                even_cur = even_cur.next
            cur = cur.next
            polar = not polar
        odd_cur.next = even.next
        return odd.next


class Solution2:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = ListNode(0)
        even = ListNode(1)
        cur = head
        odd_cur = odd
        even_cur = even
        polar = True
        while cur:
            tmp = cur.next
            cur.next = None
            if polar:
                odd_cur.next = cur
                odd_cur = odd_cur.next
            else:
                even_cur.next = cur
                even_cur = even_cur.next
            cur = tmp
            polar = not polar
        odd_cur.next = even.next
        return odd.next
