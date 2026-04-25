class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums = sorted(nums)
        res = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]: # if i is not at least 1, then nums[0] == nums[-1] doesnt make sense
                continue
            # to make nums[i] + nums[j] + nums[k] == 0, nums[j] + nums[k] must equal to - nums[i]
            j, k = i+1, len(nums)-1

            while j < k: 
                if nums[j] + nums[k] + nums[i] == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    # to avoid duplicates 
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1 
                else:
                    k -= 1

        return res
