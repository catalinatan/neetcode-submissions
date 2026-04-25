class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 
        min_val = nums[0]

        while l <= r: 
            if nums[l] <= nums[r]: 
                min_val = min(min_val, nums[l])
                break 

            mid = (l+r) // 2 
            min_val = min(min_val, nums[mid])

            if nums[l] <= nums[mid]:
                l = mid + 1 # 3 < 7 but 2 < 3 
            else: 
                r = mid - 1 
        return min_val 


            
