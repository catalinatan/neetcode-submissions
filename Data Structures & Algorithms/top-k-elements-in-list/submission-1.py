import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # usually to get frequency u use a counter to run 
        # the entire thing on nums and then make it val: frequency
        # then sorted the dictionary by items and select the top k ones

        # if we use heapify i guess can keep popping and counting the frequency
        # of each, can also just keep the top k elements in a list or smthg that
        # gets pushed

        # can heappush tuple (frequency, num), heap will try to sort by frequency if 
        # frequency is equal then they sort by number
        
        freq_dict = Counter(nums)
        print(freq_dict)
        my_heap = []
        for no, freq in freq_dict.items():
            heapq.heappush(my_heap, (-1*freq, no))
        
        print(my_heap)
        res = []
        for k_items in range(k):
            res.append(heapq.heappop(my_heap)[1])
        return res