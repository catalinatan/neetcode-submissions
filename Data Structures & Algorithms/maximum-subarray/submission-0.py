class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # use 2 pointers
        L = 0 
        curSum = 0 
        maxSum = nums[0]
        maxL, maxR = 0, 0

        for R in range(len(nums)):
            if curSum < 0: 
                curSum = 0 
                L = R
            curSum += nums[R]
            if curSum >= maxSum:
                maxSum = curSum 
                maxL, maxR = L, R
    
        return maxSum