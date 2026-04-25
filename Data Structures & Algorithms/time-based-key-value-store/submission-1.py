class TimeMap:

    def __init__(self):
        self.store = {} # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store: 
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = "" 
        values = self.store.get(key, [])

        # run binary search 
        l, r = 0, len(values)-1 

        while l <= r: 
            m = (l+r) // 2 
            
            key = values[m][0]
            mid_timestamp = values[m][1]

            if mid_timestamp <= timestamp: # want to output the most recent (max timestamp result so
            # that's why its l = m + 1 
                res = key
                l = m + 1 
            else: # mid_timestamp > timestamp
                r = m - 1 
            
        return res 
