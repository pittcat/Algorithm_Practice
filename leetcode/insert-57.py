#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals == []:
            return [newInterval]
        res = []
        for i in sorted([newInterval] + intervals, key=lambda x: x.start):
            if res and res[-1].end >= i.start:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res
