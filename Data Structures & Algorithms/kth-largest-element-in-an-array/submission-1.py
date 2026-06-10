# instead of negative numbers
# can just add heapify one by one so 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [] 
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap) # remove smallest among the k largest
        return heap[0] # root would be the largest
        