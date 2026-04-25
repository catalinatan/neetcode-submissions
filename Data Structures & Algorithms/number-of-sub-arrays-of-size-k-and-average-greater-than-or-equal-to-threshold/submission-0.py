class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0
        if not arr:
            return 0 
        
        l, r = 0, 0 
        count = 0 
        curSum = 0 

        while r < len(arr):
            curSum += arr[r]
            if r - l + 1 == k: 
                if curSum >= threshold * k:
                    count += 1 
                curSum -= arr[l] 
                l += 1 
            r += 1 
        return count