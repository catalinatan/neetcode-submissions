import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use heapify with min heap 
        stones = [-s for s in stones]
        heapq.heapify(stones)
        i = len(stones) - 1

        while len(stones) > 1: 
            y = heapq.heappop(stones) # heaviest
            x = heapq.heappop(stones) # 2nd heaviest
            if x != y:
                print(y-x)
                heapq.heappush(stones,y-x)

        return abs(stones[0]) if stones else 0
         