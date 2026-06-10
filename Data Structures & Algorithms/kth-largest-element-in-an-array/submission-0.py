import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # unsorted array nums, and integer k, return kth largest element 
        # kth largest element in sorted order
        # BUT we need to solve it without sorting

        # first, heap sorts out nums from smallest to largest
        # if u do default heappop with k elements ull get k smallest elements
        # so one way is to make the values negative so that the largest would be the first one
        # to pop out 
        # then u can just add negative sign again when u pop 

        # handle edge case
        if k > len(nums):
            return 0 

        # assume solution where u sort first 
        # turn each integer in nums to negative then make it a list before turning it into a heap
        # modifies in place so make it negative then no need to assign a new variable
        neg_nums = [-n for n in nums]
        heapq.heapify(neg_nums)

        for _ in range(k):
            largest_element = heapq.heappop(neg_nums)
            
        return -largest_element