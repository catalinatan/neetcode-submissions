class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # important info: 
        # sorted, asc by start_i 
        # task: insert interval: 
        # - sorted, asc by start_i 
        # - no overlapping interval (overlap if end_i > start_i+1), valid since sorted interval
        # - merge intervals if needed (if overlap, new_interval = [start_i, end_i+1])

        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                # newInterval ends before current starts → insert now
                res.append(newInterval)
                # then append all remaining intervals and return
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                # current ends before new starts → no overlap yet, keep it
                res.append(intervals[i])
            else:
                # overlap → merge
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res