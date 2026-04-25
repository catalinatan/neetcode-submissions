class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # unique values so needs to be with i 
            if i > 0 and a == nums[i-1]: # if current value is the same as before 
                continue # skip iteration

            l, r = i+1, len(nums)-1

            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1 
                elif threesum < 0:
                    l += 1
                else:
                    # the other pointer will update itself so this is just one pointer
                    res.append([a,nums[l],nums[r]])
                    l += 1 
                    while nums[l] == nums[l-1] and l < r:
                        l += 1 
        return res