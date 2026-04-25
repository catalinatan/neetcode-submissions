class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        min_i = 0 
        for i, n in enumerate(nums):
            if i == 0 or n != nums[i-1]:
                nums[min_i] = n 
                min_i += 1 
        return min_i