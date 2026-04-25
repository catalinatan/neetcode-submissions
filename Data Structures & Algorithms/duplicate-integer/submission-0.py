class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_set = set()
        for item in nums: 
            unique_set.add(item)

        if len(unique_set) != len(nums): 
            return True
        else:
            return False