"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Syntax: lambda <arguments>: <expression>
        # interval is the argument (the name you give to each element).
        # interval.start is the expression that returns the start value.

        intervals.sort(key=lambda interval: interval.start)
        for i in range(1, len(intervals)):
            # overlapping if start_i < end_i-1
            if intervals[i-1].end > intervals[i].start:
                return False
        return True
