"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # if any of the start times are smaller than one of the end times 
        # return false

        sorted_intervals_list = sorted(intervals, key=lambda x:x.start)
        print(sorted_intervals_list)

        end_vals = set()
        for obj in sorted_intervals_list:
            for end_val in end_vals:
                if obj.start < end_val:
                    return False
            end_vals.add(obj.end)
      
        return True
