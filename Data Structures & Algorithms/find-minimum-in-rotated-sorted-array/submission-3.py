class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force is just find min(nums)

        # rules
        # if u rotate len(nums) times, it gives original array back 
        # n times means nums[:-n] = nums[:n] move last n elements to the beginning
        # assume that elements in nums are unique

        # basically u have 2 subarrays  
        # [3,4,5,6,1,2]
        # if u find the number on the right of the left that is smaller,
        # the first one u find is the minimum 

        # can only do normal binary search if its not rotated so i guess now that its
        # rotated u can only perform binary search separately on the 2 subarrays

        # or find the middle then do while loop to keep the r go right until its smaller
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2 
            
            if nums[m] > nums[r]:
                l = m + 1 
            else:
                r = m
            
        return nums[l]