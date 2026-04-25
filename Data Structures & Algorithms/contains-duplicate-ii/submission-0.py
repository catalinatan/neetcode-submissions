class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        l, r = 0, 0
        seen = set()

        while r < len(nums):
            if r - l > k: 
                seen.remove(nums[l])
                l += 1 
            if nums[r] in seen:
                return True
            seen.add(nums[r])
            r += 1 

        return False