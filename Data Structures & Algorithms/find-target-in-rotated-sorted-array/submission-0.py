class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pos idx of target is the answer
        # add layer of comparison with target
        # which region is the target in
        # return -1 if not present in nums

        l, r = 0, len(nums)-1

        while l <= r: 
            m = (l + r)//2
            if nums[m] == target:
                return m
            if nums[m] > nums[r]:
                if nums[l] <= target < nums[m]:
                    r = m - 1 
                else:
                    l = m + 1 
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1