#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return intervals
        res = []
        for i in sorted(intervals, key=lambda x: x.start):
            if res and i.start <= res[-1].end:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)

        return res
