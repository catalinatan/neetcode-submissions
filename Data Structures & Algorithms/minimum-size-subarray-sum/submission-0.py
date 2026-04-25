class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # uses 2 pointers
        l, r = 0, 0
        curSum = 0 
        min_array = float("inf")

        while l <= r and r < len(nums):
            curSum += nums[r]
            while curSum >= target:
                min_array = min(min_array, r - l + 1)
                curSum -= nums[l]
                l += 1 
            r += 1

        return 0 if min_array == float("inf") else min_array